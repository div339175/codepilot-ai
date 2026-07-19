from fastapi import FastAPI
from app.api.routes import router
from app.api.parser import router as parser_router
from app.api.search import router as search_router
from app.api.chat import router as chat_router
from app.api.analysis import router as analysis_router
from app.api.repositories import router as repositories_router
from app.api.index import router as index_router
from app.api.search_all import router as search_all_router
from app.api.cache import router as cache_router
from app.api.dashboard import router as dashboard_router
from app.api.review import router as review_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="CodePilot AI")

app.include_router(router)
app.include_router(parser_router)
app.include_router(index_router)
app.include_router(search_router)
app.include_router(chat_router)
app.include_router(analysis_router)
app.include_router(repositories_router)
app.include_router(search_all_router)
app.include_router(cache_router)
app.include_router(dashboard_router)
app.include_router(review_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)