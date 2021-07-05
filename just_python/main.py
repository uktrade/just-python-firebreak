from .server import configure_http_server


def main():
    app = configure_http_server()
    return app
