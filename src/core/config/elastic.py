from elasticsearch import Elasticsearch
import os
ES_HOST: str = os.getenv("ES_HOST", "")

headers = {
    "Accept": "application/vnd.elasticsearch+json; compatible-with=9",
    "Content-Type": "application/vnd.elasticsearch+json; compatible-with=9"
}


INDEX_NAME: str = "avis_etudiant"
elastic_client = Elasticsearch(ES_HOST, headers=headers)
