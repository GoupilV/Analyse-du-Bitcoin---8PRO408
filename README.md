# 8PRO408 - Mini-projet: Analyse exploratoire et temporelle des données historiques du Bitcoin

Réalisé par Maïlys Demol et Victor Goupil.

## Description du projet

Ce projet vise à réaliser une analyse exploratoire et temporelle d’un ensemble de données historiques portant sur le Bitcoin. Il comprend notamment l’extraction, le traitement et la visualisation de données afin d’identifier des tendances, variations et comportements liés au marché du Bitcoin au fil du temps.

## Prérequis

Les librairies suivantes sont nécessaires au bon fonctionnement du projet :
- plotly
- seaborn
- numpy
- matplotlib
- pandas

## Installation

Après avoir cloné le dépôt Github, se déplacer dans le dossier:
```
cd Analyse-du-Bitcoin---8PRO408
```

Pour installer automatiquement l’ensemble des dépendances, veuillez exécuter la commande :
```
pip install -r requirements.txt
```

Et pour activer l'environement virtuel python si nécessaire :
```
.venv\Scripts\activate
```

## Lancement

Une fois les dépendances installées, le Notebook Jupyter peut être exécuté.

## Données

Le projet utilise un fichier CSV volumineux (environ 383.7 Mo) contenant l’historique complet des transactions Bitcoin.
Afin d’optimiser le chargement et la distribution des données, il est utilisé sous forme compressée (.zip), tel que fourni par la source originale sur Kaggle.

## Dataset

[Bitcoin Historical Data - Kaggle](https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data)

Lors de la première exécution du Notebook :
- si une copie locale du fichier CSV est détectée, elle est utilisée ;
- sinon, le fichier ZIP est extrait automatiquement.

## Application Streamlit

[Lien vers l’application Streamlit](https://analyse-du-bitcoin---8pro408git-ljrfbgppap6mmutgckxqn2.streamlit.app)

