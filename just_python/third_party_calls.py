import asyncio
import json
from typing import Any, Awaitable
from urllib import request


async def get_bank_holidays() -> dict:
    url: str = "https://www.gov.uk/bank-holidays.json"
    req_obj: request.Request = request.Request(url)

    loop: asyncio.AbstractEventLoop = asyncio.get_running_loop()
    awaitable: Awaitable[Any] = loop.run_in_executor(
        None, lambda: request.urlopen(req_obj).read()
    )
    json_str: str = await awaitable
    return json.loads(json_str)
