from fastapi import FastAPI
from app.api.routes import router
from app.api.parser import router as parser_router
from app.api.search import router as search_router
from app.api.chat import router as chat_router

app = FastAPI(title="CodePilot AI")

app.include_router(router)
app.include_router(parser_router)
app.include_router(search_router)
app.include_router(chat_router)