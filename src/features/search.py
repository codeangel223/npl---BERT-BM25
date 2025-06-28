from dataclasses import dataclass
from sklearn.metrics.pairwise import cosine_similarity
from src.shared.entities.avis import avis_data


@dataclass
class QueryAvisInMemory:
    def __init__(self):
        self.avis_contents: list[str] = [avis.content for avis in avis_data]
        self.avis_contents_embedding = [
            avis.content_encoded for avis in avis_data]

    def search(self, _query_embedded: list[float]):
        query_embedded = [_query_embedded]
        scores = cosine_similarity(
            query_embedded, self.avis_contents_embedding)[0]  # type: ignore

        top_n = 3
        top_indices = scores.argsort()[-top_n:][::-1]

        print("\n📊 Résultats similaires :")
        for i in top_indices:
            print(f"🔹 {self.avis_contents[i]}  (score: {scores[i]:.3f})")
