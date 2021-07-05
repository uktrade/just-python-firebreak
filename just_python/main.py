import aiohttp
from aiohttp import web


async def handle(request):
    name = request.match_info.get("name", "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)
async def websocket_handler(request):
    print("Websocket connection starting")
    ws = aiohttp.web.WebSocketResponse()
    await ws.prepare(request)
    print("Websocket connection ready")

    async for msg in ws:
        print(msg)
        if msg.type == aiohttp.WSMsgType.TEXT:
            print(msg.data)
            if msg.data == "close":
                print("CLOSE")
                await ws.close()
            else:
                print("SEND")
                await ws.send_str(msg.data + "/answer")

    print("Websocket connection closed")
    return ws


def main():
    app = web.Application()
    app.add_routes(
        [
            web.get("/", handle),
            web.get("/ws", websocket_handler),
            web.get("/{name}", handle),
        ]
    )
    return app
