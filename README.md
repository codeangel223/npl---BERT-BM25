# Projet BM25 + BERT pour la recherche d'avis des étudiants sur les Cours

## 🛠️ Installation

```bash
pip install -r requirements.txt
```

## 🚀 Lancement

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
