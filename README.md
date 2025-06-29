# Projet BM25 + BERT pour la recherche d'avis des étudiants sur les Cours

## 🛠️ Installation

```bash
pip install -r requirements.txt
```
## Lancement du serveur elasticsearch

```bash
docker compose up elasticsearch -d
```

## 🚀 Lancement de l'application console 

```bash
python -m run
```

## 📊 Fonctionnalités

1. **Recherche d'avis** : Recherche sémantique en français
2. **Ajout d'avis** : Ajout de nouveaux avis avec encodage automatique

## 🔧 Modèles utilisés

- **CamemBERT** : Modèle BERT spécialisé pour le français
- **Sentence-CamemBERT** : Modèle d'encodage de phrases françaises
- **Similarité cosinus** : Calcul de similarité entre vecteurs

## 📝 Exemple d'utilisation

```
1 -> Demander quelque chose
2 -> Ajouter un nouvel avis

Recherche : Le cours est trop théorique
```

Les résultats afficheront maintenant :

- Le contenu de l'avis
- Le nom de l'utilisateur
- Le module concerné
- Le score de similarité

# test queries

"""
Le prof etait pas clair dans ses explications
Le cours est trop théorique
Le professeur est très pédagogue
Manque de pratique
Contenu clair et bien structuré
Explications trop rapides
"""

## Lancer le sc
