import os
from dotenv import load_dotenv


load_dotenv()

chave = os.getenv('SECRET_KEY')