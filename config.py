from dotenv import load_dotenv
import os 
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACESS_TOKEN_MINUTES = int(os.getenv("ACESS_TOKEN_MINUTES"))
