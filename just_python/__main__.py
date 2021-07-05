from aiohttp import web

from . import main
from .db import configure_db

if __name__ == "__main__":
    configure_db()
    app = main()
    web.run_app(app)
