import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(layout="wide", page_title="Analyse Bitcoin")

# Mise en cache des données
@st.cache_data
def load_data():
    df = pd.read_parquet('data/clean/bitcoin_1h_engineered.parquet')
    return df

try:
    df_bitcoin_1h = load_data()
except Exception as e:
    st.error(f"Erreur de chargement du fichier : {e}")
    st.stop()

st.sidebar.header("Filtres temporels")

# Récupération des dates min et max
min_date = df_bitcoin_1h.index.min().date()
max_date = df_bitcoin_1h.index.max().date()

# Widget Slider
start_date, end_date = st.sidebar.slider(
    "Sélectionnez la période :",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date)
)

# Filtrage par date
mask = (df_bitcoin_1h.index.date >= start_date) & (df_bitcoin_1h.index.date <= end_date)
df_filtered = df_bitcoin_1h.loc[mask].copy()

# Notre DataFrame a trop de points, il faut donc le resampler si nécessaire
if len(df_filtered) > 10000:
    chart_data = df_filtered.resample('1D').agg({
        'open': 'first',
        'high': 'max',
        'low': 'min',
        'close': 'last',
        'volume': 'sum'
    })
    st.warning(f"Trop de données ({len(df_filtered)} points). Affichage agrégé par Jour pour la fluidité.")
else:
    chart_data = df_filtered

st.title("Analyse du Bitcoin - Maïlys Demol et Victor Goupil")

# Métriques intéressantes
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Prix Moyen", f"{df_filtered['close'].mean():.2f} $")
with col2:
    st.metric("Volume Total", f"{df_filtered['volume'].sum():,.0f}")
with col3:
    st.metric("Prix Max", f"{df_filtered['close'].max():.2f} $")

st.markdown("---")

# Courbe de prix Candlestick
st.subheader("Evolution du prix (close)")

# Calcul des bornes Y sur les données filtrées
y_min = chart_data["low"].min()
y_max = chart_data["high"].max()

fig_price = go.Figure(data=[
    go.Candlestick(
        x=chart_data.index,
        open=chart_data["open"],
        high=chart_data["high"],
        low=chart_data["low"],
        close=chart_data["close"],
        name="Bitcoin"
    )]
)

fig_price.update_layout(
    yaxis=dict(
        range=[y_min, y_max],
        tickformat="$,.0f",
        separatethousands=True,
        title="Prix (USD)",
        fixedrange=False
    ),
    xaxis=dict(
        title="Date",
        rangeslider=dict(
            visible=True,
            thickness=0.05
        ),
    ),
    height=600,
    title="Prix (close) du Bitcoin",
)

st.plotly_chart(fig_price, use_container_width=True)

st.subheader("Analyse volume et prix")

fig_combo = px.line(
    chart_data,
    x=chart_data.index,
    y="volume",
    title="Volume (gauche) et prix (droite)"
)

fig_combo.update_traces(
    name="Volume",
    line=dict(color="#1f77b4", width=1),
    opacity=0.5
)

fig_combo.add_trace(
    go.Scatter(
        x=chart_data.index,
        y=chart_data["close"],
        name="Prix",
        yaxis="y2",
        line=dict(color="#ff7f0e", width=2)
    )
)

fig_combo.update_layout(
    xaxis=dict(title="Date"),

    yaxis=dict(
        title="Volume",
        separatethousands=True
    ),

    yaxis2=dict(
        title="Prix ($)",
        overlaying="y",
        side="right",
        separatethousands=True
    ),

    hovermode="x unified",
    legend=dict(x=0, y=1.1, orientation="h")
)

st.plotly_chart(fig_combo, use_container_width=True)
