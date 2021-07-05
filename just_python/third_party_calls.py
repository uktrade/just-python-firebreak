import asyncio
import json
from urllib import request


async def get_bank_holidays():
    url = "https://www.gov.uk/bank-holidays.json"
    req_obj = request.Request(url)

    loop = asyncio.get_running_loop()
    awaitable = loop.run_in_executor(None, lambda: request.urlopen(req_obj).read())
    json_str = await awaitable
    return json.loads(json_str)
