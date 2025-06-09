from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from api.stars import router as stars_router
from mangum import Mangum

app = FastAPI()

app.include_router(stars_router, prefix="/api")
app.mount("/static", StaticFiles(directory="frontend", html=True), name="static")

@app.get("/")
def serve_index():
    return FileResponse("frontend/index.html")

handler = Mangum(app)
