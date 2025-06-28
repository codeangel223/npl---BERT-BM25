#!/bin/bash

ES_HOST="http://localhost:9200"
INDEX_NAME="avis_etudiant"

# Document 1
curl -X POST "${ES_HOST}/${INDEX_NAME}/_doc" -H 'Content-Type: application/json' -d'
{
  "user_name": "Fatou Ndiaye",
  "module": "Analyse de données",
  "content": "Le module est intéressant, mais j’aurais aimé plus d’exercices pratiques.",
  "content_encoded": null
}
'

# Document 2
curl -X POST "${ES_HOST}/${INDEX_NAME}/_doc" -H 'Content-Type: application/json' -d'
{
  "user_name": "Mohamed Diop",
  "module": "Programmation Python",
  "content": "Très bon enseignement. Le professeur est clair et les TP sont bien structurés.",
  "content_encoded": null
}
'

# Document 3
curl -X POST "${ES_HOST}/${INDEX_NAME}/_doc" -H 'Content-Type: application/json' -d'
{
  "user_name": "Aïssatou Sow",
  "module": "Intelligence Artificielle",
  "content": "Contenu riche, mais le rythme était un peu trop rapide à mon goût.",
  "content_encoded": null
}
'

# Document 4
curl -X POST "${ES_HOST}/${INDEX_NAME}/_doc" -H 'Content-Type: application/json' -d'
{
  "user_name": "Cheikh Fall",
  "module": "Base de données",
  "content": "J’ai adoré les travaux dirigés, mais le support de cours était trop théorique.",
  "content_encoded": null
}
'

# Document 5
curl -X POST "${ES_HOST}/${INDEX_NAME}/_doc" -H 'Content-Type: application/json' -d'
{
  "user_name": "Ndeye Diallo",
  "module": "Apprentissage automatique",
  "content": "Cours très complet, mais manque de clarté dans certaines explications.",
  "content_encoded": null
}
'

# Document 6
curl -X POST "${ES_HOST}/${INDEX_NAME}/_doc" -H 'Content-Type: application/json' -d'
{
  "user_name": "Ousmane Ba",
  "module": "Systèmes d’exploitation",
  "content": "Excellent module. La partie sur les processus et threads m’a beaucoup appris.",
  "content_encoded": null
}
'

# Document 7
curl -X POST "${ES_HOST}/${INDEX_NAME}/_doc" -H 'Content-Type: application/json' -d'
{
  "user_name": "Mariama Kane",
  "module": "Réseaux informatiques",
  "content": "Le formateur maîtrise bien son sujet. Quelques bugs dans les TP mais globalement satisfaisant.",
  "content_encoded": null
}
'

# Document 8
curl -X POST "${ES_HOST}/${INDEX_NAME}/_doc" -H 'Content-Type: application/json' -d'
{
  "user_name": "Ibrahima Gaye",
  "module": "DevOps",
  "content": "Formation très utile. La partie CI/CD m’a permis de mieux comprendre les pipelines.",
  "content_encoded": null
}
'
