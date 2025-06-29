#!/bin/bash

docker compose up -d

ES_HOST="http://localhost:9201"

# Nom de l'index
INDEX_NAME="avis_etudiant"

sleep 5

# Création de l'index avec mapping
curl -X PUT "${ES_HOST}/${INDEX_NAME}" -H 'Content-Type: application/json; charset=UTF-8' -d $'
{
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 1
  },
  "mappings": {
    "properties": {
      "user_name": {
        "type": "text",
        "analyzer": "standard"
      },
      "module": {
        "type": "keyword"
      },
      "content": {
        "type": "text",
        "analyzer": "standard"
      },
      "content_encoded": {
        "type": "dense_vector",
        "index": true,
        "similarity": "cosine"
      }
    }
  }
}'


# inserer quelques avis pour commencer
python -m run.insert_avis
