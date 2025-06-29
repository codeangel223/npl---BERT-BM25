from dataclasses import dataclass
from typing import Any
from src.core.config.elastic import elastic_client


@dataclass
class QueryAvisInMemory:

    def search(self, _query_embedded: list[float]):
        top_n = 5
        num_candidates = 100

        response = elastic_client.search(
            index="avis_etudiant",
            knn={
                "field": "content_encoded",
                "k": top_n,
                "num_candidates": num_candidates,
                "query_vector": _query_embedded,
            }
        )
        hits = response["hits"]["hits"]
        self.afficher_resultats(response, hits)

    def afficher_resultats(self, response: Any, hits: Any):
        print(
            f"\n📊 Résultats de recherche ({response["hits"]["total"]["value"]} résultats) :")
        print("=" * 60)

        for i, hit in enumerate(hits):
            doc = hit["_source"]
            score = hit["_score"]
            if score > 0.3:  # Seuil de pertinence
                print(f"{i}. 📝 {doc["content"]}")
                print(
                    f"   👤 {doc["user_name"]} | 📚 {doc["module"]}")
                print(f"   🎯 Score de similarité: {score:.3f}")
                print("-" * 40)
            else:
                print(f"{i}. ⚠️  Résultat peu pertinent (score: {score:.3f})")
                print(f"   📝 {doc["content"]}")
                print(
                    f"   👤 {doc["user_name"]} | 📚 {doc["module"]}")
                print("-" * 40)

        if not any(hit["_score"] > 0.3 for hit in hits):
            print(
                "❌ Aucun résultat très pertinent trouvé. Essayez de reformuler votre recherche.")
