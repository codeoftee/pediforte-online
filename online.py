from os.path import join, dirname, exists
from dotenv import load_dotenv


env_path = join(dirname(__file__), '.env')
senv_path = join(dirname(__file__), '.senv')
load_dotenv(env_path)
if exists(senv_path):
    load_dotenv(senv_path)

from base import create_app
app = create_app()

