import asyncio
from typing import Optional
from core.engine import App
from core.executor import Executor
from infra.logger import Logger


log = Logger().level


class TaskManager(Executor):

    def __init__(self, base_port: int, workers: int) -> None:
        self.base_port = base_port
        self.workers = workers

    async def main(self) -> None:

        app = App()
        tasks = []

        for worker in range(self.workers):
            log.info(f"Creating server {worker+1}")
            port = int(self.base_port) + worker
            tasks.append(app.execute(host='0.0.0.0', worker_id=worker, port=port))

        await asyncio.gather(*tasks)

    def execute(self, *args: Optional[any], **kwargs: Optional[any]) -> None:
        asyncio.run(self.main())
