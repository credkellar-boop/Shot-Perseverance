from pydantic import BaseModel
from typing import List, Optional

class ShotMetrics(BaseModel):
    release_height: float
    release_velocity: float
    rhythm_ms: int
    is_consistent: bool
    video_clip_path: Optional[str] = None
