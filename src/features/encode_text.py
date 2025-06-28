
from sentence_transformers import SentenceTransformer


class TextEncoder:
    def __init__(self,):
        self.model = SentenceTransformer(
            "paraphrase-multilingual-MiniLM-L12-v2")

    def encode(self, text_to_encode: str) -> list[float]:
        text_clean = text_to_encode.strip().lower()
        return self.model.encode(text_clean).tolist()  # type: ignore
