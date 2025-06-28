from dataclasses import dataclass
from src.shared.entities.avis import Avis, avis_data
import logging as log


@dataclass
class AvisRepository:

    def save_inmemory(self, avis: Avis):
        if not avis.is_encoded():
            log.warning("Avis non encodé !")
        avis_data.append(avis)
        print("Avis saved successful !", len(avis_data))

    def save(self, avis_to_create: Avis) -> Avis:
        # TODO: logi to create an avis
        return avis_to_create
