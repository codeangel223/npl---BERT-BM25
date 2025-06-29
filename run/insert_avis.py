
from dotenv import load_dotenv
from src.features.insert_auto_avis import insert as insert_avis_etduant_automatiquely

load_dotenv(".env", override=True)

if __name__ == "__main__":
    insert_avis_etduant_automatiquely()
