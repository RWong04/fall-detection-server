import json
from pathlib import Path

DATA_FILE = Path("data/events.json")

def ensure_data_file():
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")

def load_events():
    ensure_data_file()
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))

def save_event(event: dict):
    events = load_events()
    events.insert(0, event)
    DATA_FILE.write_text(json.dumps(events, ensure_ascii=False, indent=2), encoding="utf-8")
    return event