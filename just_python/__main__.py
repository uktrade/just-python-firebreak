from aiohttp import web

from . import main

if __name__ == "__main__":
    app = main()
    web.run_app(app)
