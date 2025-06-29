# 🔍 Projet de Recherche Sémantique d’Avis Étudiants (BM25 + BERT)

Ce projet combine la recherche traditionnelle (BM25) avec un **modèle de similarité sémantique multilingue** pour améliorer la recherche d’avis d’étudiants sur les cours, en français.

---

## ⚙️ Installation

1. **Créer un environnement virtuel** (recommandé) :

```bash
python -m venv venv
source venv/bin/activate     # Linux / macOS
venv\Scripts\activate        # Windows
```

2. **Installer les dépendances** :

```bash
pip install -r requirements.txt
```

---

## 🚀 Lancer l’application

1. **Initialiser les données / l’environnement** :

```bash
./setup.sh
```

2. **Lancer l’application en console** :

```bash
python -m run
```

---

## 📌 Fonctionnalités

- 🔍 **Recherche d’avis** : recherche sémantique en français
- ➕ **Ajout d’avis** : enregistrement de nouveaux avis, encodés automatiquement

---

## 🧠 Modèle utilisé

- **Distiluse-base-multilingual-cased** :
  Un modèle léger et multilingue (dont le français) basé sur `distilBERT`, proposé par [Sentence-Transformers](https://www.sbert.net).

- **Similarité cosinus** :
  Mesure de la proximité entre les vecteurs d’avis.

---

## 💬 Exemple d’utilisation (Console)

```
1 -> Demander quelque chose
2 -> Ajouter un nouvel avis

Recherche : Le cours est trop théorique
```

Les résultats afficheront :

- 📄 Contenu de l’avis
- 👤 Nom de l'étudiant
- 📘 Module concerné
- 📈 Score de similarité (entre 0 et 1)

---

## 🧪 Exemples de requêtes à tester

```
Le prof était pas clair dans ses explications
Le cours est trop théorique
Le professeur est très pédagogue
Manque de pratique
Contenu clair et bien structuré
Explications trop rapides
```

---
