import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from api.stars import router as stars_router
from mangum import Mangum

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = FastAPI()

app.include_router(stars_router, prefix="/api")

frontend_path = os.path.join(BASE_DIR, "public")
app.mount("/static", StaticFiles(directory=frontend_path, html=True), name="static")

@app.get("/")
def serve_index():
    return FileResponse(os.path.join(frontend_path, "index.html"))

handler = Mangum(app)
