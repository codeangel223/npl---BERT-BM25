# 🎓 Projet : Recherche Sémantique d’Avis Étudiants

### (BM25 + BERT dans le cadre du cours de NLP)

---

## 🧾 Contexte pédagogique

Ce projet a été réalisé dans le cadre du **cours de Natural Language Processing (NLP)**.  
L'objectif pédagogique était de concevoir un système de recherche d'information performant combinant :

- 🔍 **BM25**, une méthode de recherche lexicale (via Elasticsearch)
- 🧠 **Embeddings contextualisés**, à l’aide d’un modèle de type BERT

> 👉 Le sujet nous invitait à proposer une **solution hybride** capable de mieux interpréter le sens des phrases, en particulier dans le cadre d’une **application concrète**.

---

## 🎯 Sujet du projet

Nous avons choisi de travailler sur le **traitement des avis d’étudiants sur leurs cours**.  
Ces avis sont souvent :

- Rédigés en langage naturel (et donc subjectifs)
- Riches en ressentis, mais difficiles à analyser automatiquement
- Très variés en formulation

### Notre mission :

> Concevoir un moteur de recherche capable de **retrouver automatiquement les avis les plus similaires** à une phrase saisie, en **comprenant le sens**, pas uniquement les mots.

---

## 🧠 Les outils que nous avons utilisés

### 🔤 BERT : un modèle de langage contextuel

BERT (Bidirectional Encoder Representations from Transformers) est un modèle de langage développé par Google.  
Il comprend les phrases en tenant compte du **contexte des mots** (avant et après).

🔎 Exemple :

> “Ce cours manque de pratique” ≠ “C’est un cours très pratique”

---

### 🧠 Sentence Transformers : l’encodage de phrases

Nous avons utilisé la librairie `sentence-transformers` et le modèle :  
📌 `distiluse-base-multilingual-cased`

Ce modèle transforme une phrase en **vecteur numérique** (embedding), ce qui permet ensuite de :

- Comparer des phrases entre elles
- Mesurer leur **similarité sémantique** via la **cosine similarity**

---

### 🔎 BM25 : la recherche classique dans les documents

BM25 est un algorithme utilisé par les moteurs de recherche (notamment via **Elasticsearch**).

Il fonctionne en :

- Comparant les mots de la requête à ceux des documents
- Calculant une **pertinence lexicale** en fonction de la fréquence des mots

> 📌 C’est rapide et efficace… mais ça ne comprend pas le sens !

---

## 🔀 La solution hybride que nous avons construite

Notre système combine :

1. ✅ **BM25**, pour une première sélection rapide d’avis pertinents
2. ✅ **Embeddings BERT**, pour reclasser les résultats selon leur **proximité sémantique réelle**

### Étapes :

- Encodage de tous les avis existants avec le modèle `distiluse-base-multilingual-cased`
- Lors d’une recherche :
  - La requête est encodée
  - On compare son embedding à ceux des avis existants
  - On classe les résultats selon leur **score de similarité cosinus**

---

## 💬 Cas d’usage

| Requête étudiante                       | Résultats retournés                     |
| --------------------------------------- | --------------------------------------- |
| “Le cours était trop théorique”         | “Il manque de pratique”                 |
| “Je n’ai rien compris aux explications” | “Les explications étaient trop rapides” |
| “Bon professeur”                        | “Très pédagogue et clair”               |

✅ Les résultats sont pertinents **même quand les mots sont différents**, car le sens est compris.

---

## 📊 Résultats obtenus

Pour chaque requête, le système affiche :

- 📄 Le texte de l’avis retrouvé
- 📘 Le module concerné
- 👤 Le nom de l'étudiant
- 📈 Un score de similarité (entre 0 et 1)

> Plus le score est proche de 1, plus l’avis est pertinent par rapport à la requête.

---

## 🧪 Exemple de requêtes testées

Le prof n’explique pas bien  
Le cours est trop théorique  
Pas assez d’exemples  
Trop de pratique  
Manque de structure  
Contenu bien expliqué

---

## 🔮 Perspectives d’évolution

- Création d’une **interface Web** pour rendre l’outil accessible à un plus large public
- Génération automatique de **rapports pédagogiques** à partir des avis
- Intégration de **l’analyse de sentiment** (positif, négatif, neutre)
- Extension à d’autres domaines : retour client, feedback produit, etc.

---

## 👥 Membres du groupe

Ce projet a été conçu et réalisé par notre groupe dans le cadre du cours de NLP :

- Moussa Mallé
- Arthur
- Maxies
- Adji Fatou
- Maurice

---

## 🔗 Lien vers le dépôt GitHub

➡️ [https://github.com/codeangel223/npl---BERT-BM25](https://github.com/codeangel223/npl---BERT-BM25)

---

> Merci pour votre attention 🙏  
> Ce projet illustre l’intérêt des approches hybrides en NLP pour mieux comprendre le **langage humain** dans des contextes réels.
