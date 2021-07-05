import json
import time
from pathlib import Path

import aiohttp
from aiohttp import web

from .third_party_calls import get_bank_holidays


async def handle(request):
    p = Path(".").absolute()
    html_file = p / "data" / "index.html"
    text = html_file.read_text()
    return web.Response(text=text, content_type="text/html")


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
                return

            print("SEND")
            await ws.send_str(msg.data + "/answer")
            # wait 3 seconds and then make a push to the browser
            time.sleep(3)
            bh_data = await get_bank_holidays()
            await ws.send_str(json.dumps(bh_data))

    print("Websocket connection closed")
    return ws


def configure_http_server():
    app = web.Application()
    app.add_routes(
        [
            web.get("/", handle),
            web.get("/ws", websocket_handler),
            web.get("/{name}", handle),
        ]
    )
    return app
