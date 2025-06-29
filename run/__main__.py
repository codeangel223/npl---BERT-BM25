from src.app.cli_app import run_cli_app
from dotenv import load_dotenv
from src.features.insert_auto_avis import insert as insert_avis_etduant_automatiquely

load_dotenv(".env")

if __name__ == "__main__":
    run_cli_app()
    #insert_avis_etduant_automatiquely()
