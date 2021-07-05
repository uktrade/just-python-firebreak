from .db import configure_db
from .server import configure_http_server


def main():
    app = configure_http_server()
    configure_db()
    return app
