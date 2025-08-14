from dotenv import load_dotenv
import os

SECRET_KEY=os.getenv('SECRET_KEY')
API_KEY_GOOGLE = os.getenv('API_KEY_GOOGLE')
URL_GOOGLE = os.getenv('URL_GOOGLE')