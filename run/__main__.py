from src.app.cli_app import run_cli_app
from dotenv import load_dotenv

load_dotenv(".env", override=True)

if __name__ == "__main__":
    run_cli_app()
