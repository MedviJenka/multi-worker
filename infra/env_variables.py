import os
from enum import Enum
from dotenv import load_dotenv


load_dotenv()


class Config(Enum):
    BASE_PORT = os.getenv('BASE_PORT')
    WORKERS = os.getenv('WORKERS')
