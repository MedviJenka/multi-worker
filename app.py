from core.manager import TaskManager
from infra.env_variables import Infra, Ports
from infra.logger import Logger


log = Logger().level
WORKERS = int(Infra.WORKERS.value)
BASE_PORT = int(Ports.PORT.value)
HOST = Ports.HOST.value


def main() -> None:
    task_manager = TaskManager(host=HOST, base_port=BASE_PORT, workers=WORKERS)
    task_manager.execute()


if __name__ == "__main__":
    main()
