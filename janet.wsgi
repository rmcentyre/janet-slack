
import os
import sys
import dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)

PROJECT_PATH = os.getenv('PROJECT_PATH', os.curdir)

if PROJECT_PATH not in sys.path:
    sys.path.append(PROJECT_PATH)

from app import app as application
