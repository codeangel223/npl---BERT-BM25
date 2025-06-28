from dataclasses import dataclass
from src.shared.entities.avis import Avis
import logging as log
from typing import Any
import uuid
from src.core.config.elastic import INDEX_NAME, ES_HOST
import requests


@dataclass
class AvisRepository:

    def save(self, avis: Avis):
        if not avis.is_encoded():
            log.warning("Avis non encodé !")

        payload: dict[str, Any] = {
            "user_name": avis.user_name,
            "module": avis.module,
            "content": avis.content,
            "content_encoded": avis.content_encoded,
        }

        response = requests.put(url=ES_HOST+f"/{INDEX_NAME}/_doc/{str(uuid.uuid4())}", json=payload, headers={
            "Content-Type": "application/json",
            "Accept": "application/vnd.elasticsearch+json"
        })

        if response.status_code == 201:
            print("Avis saved successful !")
        else:
            print("Avis save failed !")
