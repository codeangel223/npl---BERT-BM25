from dataclasses import dataclass
from sklearn.metrics.pairwise import cosine_similarity
from src.shared.entities.avis import avis_data


@dataclass
class QueryAvisInMemory:
    def __init__(self):
        self.avis_contents: list[str] = [avis.content for avis in avis_data]
        self.avis_contents_embedding = [
            avis.content_encoded for avis in avis_data]
        self.avis_modules: list[str] = [avis.module for avis in avis_data]
        self.avis_users: list[str] = [avis.user_name for avis in avis_data]

    def search(self, _query_embedded: list[float]):
        query_embedded = [_query_embedded]
        scores = cosine_similarity(
            query_embedded, self.avis_contents_embedding)[0]  # type: ignore

        top_n = 5
        top_indices = scores.argsort()[-top_n:][::-1]

        print(f"\n📊 Résultats de recherche ({len(top_indices)} résultats) :")
        print("=" * 60)

        for i, idx in enumerate(top_indices, 1):
            score = scores[idx]
            if score > 0.3:  # Seuil de pertinence
                print(f"{i}. 📝 {self.avis_contents[idx]}")
                print(
                    f"   👤 {self.avis_users[idx]} | 📚 {self.avis_modules[idx]}")
                print(f"   🎯 Score de similarité: {score:.3f}")
                print("-" * 40)
            else:
                print(f"{i}. ⚠️  Résultat peu pertinent (score: {score:.3f})")
                print(f"   📝 {self.avis_contents[idx]}")
                print(
                    f"   👤 {self.avis_users[idx]} | 📚 {self.avis_modules[idx]}")
                print("-" * 40)

        if not any(scores[idx] > 0.3 for idx in top_indices):
            print(
                "❌ Aucun résultat très pertinent trouvé. Essayez de reformuler votre recherche.")
