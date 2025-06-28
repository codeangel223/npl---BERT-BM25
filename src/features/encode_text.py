from sentence_transformers import SentenceTransformer
from src.core.libs.bert import sentence_transformer_model


class TextEncoder:
    def __init__(self,):
        self.model = sentence_transformer_model

    def encode(self, text_to_encode: str) -> list[float]:
        text_clean = text_to_encode.strip()
        return self.model.encode(text_clean).tolist()
