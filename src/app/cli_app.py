
from src.shared.entities.avis import Avis
from typing import Callable, Literal
from src.features.encode_text import TextEncoder
from src.features.save_avis import AvisRepository
from src.features.search import QueryAvisInMemory

MenuKey = Literal["1", "2"] | str

menu: dict[MenuKey, str] = {
    "1": "Demander quelqchose",
    "2": "Ajouter un nuvel avis",
}


def demander_quelque_chose() -> None:
    query = input("Recherche : ")
    text_encoder = TextEncoder()
    query_vector = text_encoder.encode(query)
    query_avis = QueryAvisInMemory()
    query_avis.search(query_vector)


def ajouter_avis() -> None:
    user_name: str = input("Votre Nom: ")
    module_name: str = input("Quel module: ")
    user_avis: str = input(f"Votre Avis sur {module_name}: ")
    avis_obj: Avis = Avis(user_name, module_name, user_avis,)
    text_encoder = TextEncoder()
    text_encoded = text_encoder.encode(avis_obj.content)
    avis_obj.encode_avis(text_encoded)
    avis_repo = AvisRepository()
    avis_repo.save_inmemory(avis_obj)


menu_actions: dict[MenuKey, Callable[[], None]] = {
    "1": demander_quelque_chose,
    "2": ajouter_avis,
}


def afficher_menu():
    [print(k, " -> ", menu_item) for k, menu_item in menu.items()]


def run_cli_app():
    while True:
        afficher_menu()
        query = input("Selectionner : ")
        menu_actions[query]()
