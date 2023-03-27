from dotenv import load_dotenv
import os 

load_dotenv()

def process():
    env = {
        "DATABASE_NAME": os.getenv("DATABASE_NAME"),
        "HOST": os.getenv("HOST"),
        "PORT": os.getenv("PORT"),
        "USER": os.getenv("USER"),
        "PASS": os.getenv("PASS")
    }
    return env
