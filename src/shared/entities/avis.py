from dataclasses import dataclass
from typing import List, Any


@dataclass
class Avis:
    user_name: str  # Nom etudiant
    module: str
    content: str
    id: str | None = None
    content_encoded: List[Any] | None = None

    def is_encoded(self) -> bool:
        return self.content_encoded != None

    def encode_avis(self, embedding: List[Any]):
        self.content_encoded = embedding


avis_data = []
