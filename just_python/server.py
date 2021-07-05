import json
import time
from pathlib import Path

import aiohttp
from aiohttp import web

from .db import get_call_count, increament_call_count
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
            await ws.send_str(msg.data + " Initial response answer")
            time.sleep(2)

            # interleaving synchronous and asynchronous code
            count = get_call_count()
            await ws.send_str(f"Call count {count} 3 seconds till json call")
            time.sleep(1)
            count = increament_call_count()
            await ws.send_str(f"Call count {count} 2 seconds till json call")
            time.sleep(1)
            count = increament_call_count()
            await ws.send_str(f"Call count {count} 1 seconds till json call")
            time.sleep(1)
            count = increament_call_count()
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
