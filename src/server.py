import contextlib
from fastapi import FastAPI
from catagorize import mcp as catagorize_mcp
from parser import mcp as parser_mcp
import os


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    async with contextlib.AsyncExitStack() as stack:
        await stack.enter_async_context(catagorize_mcp.session_manager.run())
        await stack.enter_async_context(parser_mcp.session_manager.run())
        yield


app = FastAPI(lifespan=lifespan)
app.mount("/catagorize", catagorize_mcp.streamable_http_app())
app.mount("/parser", parser_mcp.streamable_http_app())

PORT = os.environ.get("PORT", 10000)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)