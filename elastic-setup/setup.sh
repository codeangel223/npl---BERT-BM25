#!/bin/bash

# Adresse de ton instance Elasticsearch
ES_HOST="http://localhost:9201"

# Nom de l'index
INDEX_NAME="avis_etudiant"

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
        "type": "dense_vector"
      }
    }
  }
}'
