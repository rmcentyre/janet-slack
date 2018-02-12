
import os
import sys
import dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)

PROJECT_PATH = os.environ['PROJECT_PATH']

if PROJECT_PATH not in sys.path:
    sys.path.append(PROJECT_PATH)

from janet-slack import app as application
