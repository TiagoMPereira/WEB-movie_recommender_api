import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
        
    mongo_user = os.getenv("MONGO_USER")
    mongo_password = os.getenv("MONGO_PASSWORD")
    mongo_client = os.getenv("MONGO_CLIENT")
    mongo_db = os.getenv("MONGO_DB")

    movie_path = os.getenv("MODEL_PATH")