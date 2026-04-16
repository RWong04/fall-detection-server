from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers.events import router as events_router
from app.routers.pages import router as pages_router

app = FastAPI(title="Fall Detection Server")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(events_router)
app.include_router(pages_router)

@app.get("/")
def root():
    return {"message": "server is running"}