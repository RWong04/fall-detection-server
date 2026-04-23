from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

from app.storage import load_events

TZ = ZoneInfo("Asia/Taipei")

def format_dt(value):
    if not value:
        return "-"
    if isinstance(value, str):
        try:
            if "Z" in value:
                value = value.replace("Z", "+00:00")
            value = datetime.fromisoformat(value)
        except ValueError:
            return value
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    return value.astimezone(TZ).strftime("%Y-%m-%d %H:%M:%S")

router = APIRouter(tags=["pages"])
templates = Jinja2Templates(directory="templates")
templates.env.globals["format_dt"] = format_dt

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