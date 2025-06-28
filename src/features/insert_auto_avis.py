
from src.features.encode_text import TextEncoder
from src.shared.entities.avis import Avis
from src.features.save_avis import AvisRepository


text_encoder = TextEncoder()


def construct_avis(avis: Avis) -> Avis:
    embedding = text_encoder.encode(avis.content)
    n_avis: Avis = Avis(avis.user_name, avis.module, avis.content, )
    n_avis.encode_avis(embedding)
    return n_avis


avis_data = [
    construct_avis(Avis(user_name="moussa", module="Java avancé",
                        content="Le cours est trop théorique, on manque de pratique.")),
    construct_avis(Avis(user_name="ibrahima", module="Java avancé",
                        content="Le prof ne suit pas le plan du cours.")),
    construct_avis(Avis(user_name="cheikh", module="Réseaux",
                        content="Je n’ai pas compris les explications, trop rapides.")),
    construct_avis(Avis(user_name="aminata", module="Python",
                        content="Très bon module, les projets sont stimulants.")),
    construct_avis(Avis(user_name="khadija", module="Système",
                        content="Le TP était très utile, mais la documentation manquait.")),
    construct_avis(Avis(user_name="moussa", module="Sécurité informatique",
                        content="Cours intéressant mais un peu dense.")),
    construct_avis(Avis(user_name="aïssatou", module="UX/UI",
                        content="Trop d’exemples et pas assez de concepts.")),
    construct_avis(Avis(user_name="bocar", module="Data Science",
                        content="Le contenu est clair et bien structuré.")),
    construct_avis(Avis(user_name="youssouf", module="Mathématiques",
                        content="Le prof est très pédagogue, j’ai aimé.")),
    construct_avis(Avis(user_name="fatou", module="Cloud",
                        content="Pas assez de cas pratiques sur AWS.")),
]


def insert():
    avis_repo = AvisRepository()
    for avis in avis_data:
        avis_repo.save(avis)


if __name__ == "__main__":
    insert()
