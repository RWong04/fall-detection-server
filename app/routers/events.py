from datetime import datetime
from fastapi import APIRouter
from app.schemas import FallEvent
from app.storage import load_events, save_event

router = APIRouter(prefix="/api", tags=["events"])

@router.post("/fall-event")
def receive_fall_event(event: FallEvent):
    record = event.model_dump()
    record["received_at"] = datetime.utcnow().isoformat()
    save_event(record)
    return {"ok": True, "event": record}

@router.get("/events")
def get_events():
    return {"events": load_events()}