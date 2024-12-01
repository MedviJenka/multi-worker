from core.engine import App
from infra.env_variables import Infra, Ports
from infra.logger import Logger


log = Logger().level
WORKERS = int(Infra.WORKERS.value) + 1
BASE_PORT = int(Ports.PORT.value)
HOST = Ports.HOST.value


async def main() -> None:

    app = App()
    tasks = []

    for worker in range(1, WORKERS):
        log.info(f"Creating server {worker}")
        port = BASE_PORT + worker
        tasks.append(app.execute(host=HOST, worker_id=worker, port=port))

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
