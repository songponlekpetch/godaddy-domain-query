from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path(str(Path(".env").resolve()))
load_dotenv(dotenv_path=env_path)


GO_DADDY_API_URL = os.getenv("GO_DADDY_API_URL")
GO_DADDY_API_KEY = os.getenv("GO_DADDY_API_KEY")
GO_DADDY_API_SECRET = os.getenv("GO_DADDY_API_SECRET")
