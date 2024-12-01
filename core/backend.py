import uuid
from flask import request
from httpx import Response, AsyncClient
from infra.logger import Logger


class RequestHandler(Logger):

    """this class handles different request methods"""

    @property
    def generate_id(self) -> str:
        """Generate a unique ID using uuid4."""
        return str(uuid.uuid4())

    def get_worker_id(self, worker: int) -> str:
        self.level.info(f'worker: {worker}, id: {self.generate_id}')
        return f"Server-{worker} (id: {self.generate_id})"

    @property
    def get_url(self) -> str:
        return request.args.get('q')

    async def get_response(self) -> Response:
        """async HTTP GET request."""
        async with AsyncClient() as client:
            response = await client.get(self.get_url)
            self.level.info(f'response: {response}')
            return response
