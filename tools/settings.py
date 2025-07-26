import os
from pathlib import Path

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DEV_MODE = os.getenv('DEBUG') == '1'

BASE_DIR = Path(__file__).resolve().parent.parent

DB_DIR = BASE_DIR / 'dbs'

DATA_DIR =  BASE_DIR / 'files'

LOG_DIR =  BASE_DIR / 'logs'
