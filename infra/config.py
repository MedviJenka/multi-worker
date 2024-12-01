from infra.env_variables import Infra, Ports


class Config:
    WORKERS = int(Infra.WORKERS.value)
    BASE_PORT = int(Ports.PORT.value)
    HOST = Ports.HOST.value
