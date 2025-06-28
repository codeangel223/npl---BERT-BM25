# Projet BM25 + BERT pour la recherche d'avis

## 🚀 Améliorations récentes

### Modèle BERT français optimisé
- **Remplacement** du modèle `bert-base-uncased` (anglais) par `camembert-base` (français)
- **Amélioration** de l'encodage avec `dangvantuan/sentence-camembert-large` spécialisé pour le français
- **Préservation** des accents et de la casse française (plus de `.lower()`)

### Améliorations de la recherche
- **Plus de résultats** : affichage de 5 résultats au lieu de 3
- **Seuil de pertinence** : filtrage des résultats avec score < 0.3
- **Métadonnées enrichies** : affichage du nom d'utilisateur et du module
- **Interface améliorée** : meilleure présentation des résultats

## 🛠️ Installation

```bash
pip install -r requirements.txt
```

## 🧪 Test du modèle français

```bash
python test_bert_french.py
```

## 🚀 Lancement

```bash
python run.py
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
