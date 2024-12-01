import os
from enum import Enum
from dotenv import load_dotenv


load_dotenv()


class Ports(Enum):
    HOST = os.getenv('HOST')
    PORT = os.getenv('BASE_PORT')


class Infra(Enum):
    WORKERS = os.getenv('WORKERS')
