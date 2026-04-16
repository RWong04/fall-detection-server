from pydantic import BaseModel

class FallEvent(BaseModel):
    device_id: str
    timestamp: str
    status: str
    acc_magnitude: float | None = None
    gyro_magnitude: float | None = None