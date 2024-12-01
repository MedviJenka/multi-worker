import socket
from dotenv import load_dotenv
from flask import Flask
from hypercorn.asyncio import serve
from hypercorn.config import Config
from core.backend import RequestHandler
from core.executor import Executor
from infra.logger import Logger
from httpx import RequestError


log = Logger().level
load_dotenv()


class App(RequestHandler, Executor):

    def __init__(self) -> None:
        self.store_ids = []

    def create_app(self, worker_id: int) -> callable:

        """Create a Flask app for a given worker."""
        app = Flask(self.get_worker_id(worker_id))

        @app.route("/")
        async def home() -> str:
            return f"Hello from {self.get_worker_id(worker=worker_id)}!"

        @app.route('/api/dns', methods=['GET'])
        async def get_domain_name() -> str or dict:
            try:
                response = await self.get_response()
                response.raise_for_status()
                domain = self.get_url.split('www.')[1].split('/')[0]
                log.info(f"Domain: {domain}")
                return f"Domain: {domain}"

            except RequestError as e:
                log.error(f"HTTP error occurred: {e}")
                return {"error": str(e)}

        @app.route('/api/ip', methods=['GET'])
        async def get_domain_ip() -> dict:

            if self.get_url.startswith("http://")[7:]:
                port = 80
            else:
                port = 443

            domain = self.get_url.split('/')[0]

            try:

                ip_address = socket.gethostbyname(domain)
                log.info(f"IP address: {ip_address}, Port: {port}")

                return {
                    'ip': ip_address,
                    'port': port
                }
            except socket.gaierror:
                log.error("Unable to resolve domain.")
                return {"error": "Unable to resolve domain."}

        return app

    async def execute(self, host: str, worker_id: int, port: int) -> None:
        """Run a Flask server on a specific port."""
        app = self.create_app(worker_id)
        config = Config()
        config.bind = [f"{host}:{port}"]
        await serve(app, config)
