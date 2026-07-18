from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="CodePilot AI")

app.include_router(router)