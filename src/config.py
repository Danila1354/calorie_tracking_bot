from dotenv import load_dotenv
import os

load_dotenv()  # Загружает переменные из .env файла

TOKEN = os.getenv("TOKEN")
admins_id = list(map(int,os.getenv("admins_id").split(',')))