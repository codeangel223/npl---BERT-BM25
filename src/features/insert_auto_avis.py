
from src.features.encode_text import TextEncoder
from src.shared.entities.avis import Avis
from src.features.save_avis import AvisRepository


text_encoder = TextEncoder()


def construct_avis(avis: Avis) -> Avis:
    embedding = text_encoder.encode(avis.content)
    n_avis: Avis = Avis(avis.user_name, avis.module, avis.content, id=avis.id)
    n_avis.encode_avis(embedding)
    return n_avis


avis_data = [
    construct_avis(Avis(user_name="moussa", module="Java avancé",
                        content="Le cours est trop théorique, on manque de pratique.",
                        id="e1a3a264-234a-4e69-8f84-9dbbc5fa1447")),
    construct_avis(Avis(user_name="ibrahima", module="Java avancé",
                        content="Le prof ne suit pas le plan du cours.",
                        id="b2f3b2d4-15bb-48dd-b604-b089c73c870a")),
    construct_avis(Avis(user_name="cheikh", module="Réseaux",
                        content="Je n’ai pas compris les explications, trop rapides.",
                        id="5e8eeb5b-867d-4b75-9c2e-f6486e170abc")),
    construct_avis(Avis(user_name="aminata", module="Python",
                        content="Très bon module, les projets sont stimulants.",
                        id="9c45ad0c-9219-46cb-85ff-2b78b92920a2")),
    construct_avis(Avis(user_name="khadija", module="Système",
                        content="Le TP était très utile, mais la documentation manquait.",
                        id="3e1dba1e-2928-4a58-805c-406e92c22290")),
    construct_avis(Avis(user_name="moussa", module="Sécurité informatique",
                        content="Cours intéressant mais un peu dense.",
                        id="fd23dc68-6ab9-4a3f-a5f6-0cfb63d6dff2")),
    construct_avis(Avis(user_name="aïssatou", module="UX/UI",
                        content="Trop d’exemples et pas assez de concepts.",
                        id="d1eb9797-3d6f-4b12-8f2b-0c11cde2a13a")),
    construct_avis(Avis(user_name="bocar", module="Data Science",
                        content="Le contenu est clair et bien structuré.",
                        id="a3e2157f-0ed1-4db1-b5d7-61a97b967f2b")),
    construct_avis(Avis(user_name="youssouf", module="Mathématiques",
                        content="Le prof est très pédagogue, j’ai aimé.",
                        id="f4c03aa5-5c60-4c18-b2b0-0fca2d8cc2d1")),
    construct_avis(Avis(user_name="fatou", module="Cloud",
                        content="Pas assez de cas pratiques sur AWS.",
                        id="bb1b79b3-e56c-4746-9b5a-2d7e89e97f53")),
]


def insert():
    avis_repo = AvisRepository()
    for avis in avis_data:
        avis_repo.save(avis)


if __name__ == "__main__":
    insert()
