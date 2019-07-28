from starlette.responses import PlainTextResponse
from starlette.endpoints import HTTPEndpoint


class Homepage(HTTPEndpoint):
    async def get(self, request):
        body = await request.body()
        return PlainTextResponse(f"Request body is: {body}")
