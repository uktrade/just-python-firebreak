import asyncio
from pprint import pprint


class EchoServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info("peername")
        print("Connection from {}".format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        pprint(f"Data received: {message}")
        pprint(f"Send: {message}")

        self.transport.write(data)

        print("Close the client socket")
        self.transport.close()


async def main():
    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    loop = asyncio.get_running_loop()

    server = await loop.create_server(lambda: EchoServerProtocol(), "127.0.0.1", 8888)

    async with server:
        await server.serve_forever()
