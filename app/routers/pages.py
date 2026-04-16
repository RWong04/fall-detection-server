from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.storage import load_events

router = APIRouter(tags=["pages"])
templates = Jinja2Templates(directory="templates")

@router.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    events = load_events()
    return templates.TemplateResponse(
        request,
        "dashboard.html",
        {
            "events": events
        }
    )