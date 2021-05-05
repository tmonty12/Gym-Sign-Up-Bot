import os
from dotenv import load_dotenv

load_dotenv(override=True)

DRIVER_PATH = os.getenv('DRIVER_PATH')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
BASEMENT_URL = os.getenv('BASEMENT_URL')
SECOND_FLOOR_URL = os.getenv('SECOND_FLOOR_URL')
FIRST_FLOOR_URL = os.getenv('FIRST_FLOOR_URL')
ERNIE_URL = os.getenv('ERNIE_URL')

