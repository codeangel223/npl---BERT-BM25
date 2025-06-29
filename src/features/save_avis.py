from dataclasses import dataclass
from src.shared.entities.avis import Avis
import logging as log
from typing import Any
from src.core.config.elastic import elastic_client,  INDEX_NAME
import uuid


@dataclass
class AvisRepository:

    def save(self, avis: Avis):
        if not avis.is_encoded():
            log.warning("Avis non encodé !")

        avis_id = avis.id if avis.id else str(uuid.uuid4())

        doc: dict[str, Any] = {
            "user_name": avis.user_name,
            "module": avis.module,
            "content": avis.content,
            "content_encoded": avis.content_encoded,
        }
        elastic_client.update(
            index=INDEX_NAME,
            id=avis_id,
            doc=doc,
            doc_as_upsert=True
        )

        print("Avis saved successful !")
