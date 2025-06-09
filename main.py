from fastapi import FastAPI
from api.stars import router as stars_router
from mangum import Mangum

app = FastAPI()
app.include_router(stars_router, prefix="/api")

handler = Mangum(app)
