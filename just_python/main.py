from aiohttp.web import Application

from .db import configure_db
from .server import configure_http_server


def main() -> Application:
    configure_db()
    app: Application = configure_http_server()
    return app
