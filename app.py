from core.manager import TaskManager
from infra.env_variables import Config
from infra.logger import Logger


log = Logger()


def main() -> None:

    try:
        task_manager = TaskManager(base_port=Config.BASE_PORT.value, workers=int(Config.WORKERS.value))
        log.level.info(f'task is being executed: with the next parameters:'
                       f'base_port={Config.BASE_PORT}, workers={Config.WORKERS}')
        task_manager.execute()

    except Exception as e:
        log.level.error(f'ERROR: {e}')
        raise e


if __name__ == "__main__":
    main()
