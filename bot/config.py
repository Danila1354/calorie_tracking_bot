from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()  # Загружает переменные из .env файла

TOKEN = os.getenv("TOKEN")
admins_id = list(map(int, os.getenv("admins_id").split(',')))
data_dir = Path(__file__).resolve().parent.parent / "data" / "users"
