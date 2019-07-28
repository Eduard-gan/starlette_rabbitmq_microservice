import asyncio

import uvicorn
from starlette.applications import Starlette

from http_endpoints import Homepage
from message_consumers import all_consumers


# Routing configuration from main Starlette app
app = Starlette(debug=True)
app.add_route('/', Homepage)


@app.on_event('startup')  # Hook up message consuming to work in same event loop in parallel to Starlette app.
async def start_message_consuming():
    asyncio.ensure_future(asyncio.gather(*all_consumers), loop=asyncio.get_event_loop())


# Programmatic server launch
if __name__ == "__main__":
    uvicorn.run(app)
