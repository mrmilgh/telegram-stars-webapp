from fastapi import FastAPI
from api.stars import router as stars_router

app = FastAPI()

app.include_router(stars_router, prefix="/api")
