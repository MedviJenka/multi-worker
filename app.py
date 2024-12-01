from core.manager import TaskManager
from infra.config import Config
from infra.logger import Logger


log = Logger()
config = Config()


def main() -> None:

    try:
        task_manager = TaskManager(host=config.HOST, base_port=config.BASE_PORT, workers=config.WORKERS)
        log.level.info(f'task is being executed: with the next parameters:'
                       f' host={config.HOST}, base_port={config.BASE_PORT}, workers={config.WORKERS}')
        task_manager.execute()

    except Exception as e:
        log.level.error(f'ERROR: {e}')
        raise e


if __name__ == "__main__":
    main()
