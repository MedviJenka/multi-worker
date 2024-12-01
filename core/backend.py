import uuid
from flask import request
from httpx import Response, AsyncClient
from infra.env_variables import Infra


class RequestHandler:
    @property
    def generate_id(self) -> str:
        """Generate a unique ID using uuid4."""
        return str(uuid.uuid4())

    def get_worker_id(self, worker: Infra) -> str:
        return f"Server-{worker}-{self.generate_id}"

    @property
    def get_url(self) -> str:
        return request.args.get('q')

    async def get_response(self) -> Response:
        """Perform an async HTTP GET request."""
        async with AsyncClient() as client:
            response = await client.get(self.get_url)
            return response
