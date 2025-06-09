from fastapi import FastAPI
from api.stars import router as stars_router
from vercel_fastapi import VercelFastAPI

app = FastAPI()
app.include_router(stars_router, prefix="/api")

# Adapter برای Vercel
handler = VercelFastAPI(app)
