from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

load_dotenv(".env", override=True)

ES_HOST: str = os.getenv("ES_HOST", "")

headers = {
    "Accept": "application/vnd.elasticsearch+json",
    "Content-Type": "application/vnd.elasticsearch+json"
}

INDEX_NAME: str = "avis_etudiant"
elastic_client = Elasticsearch(ES_HOST, headers=headers)
