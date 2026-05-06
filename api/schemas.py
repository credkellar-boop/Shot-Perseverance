from pydantic import BaseModel
from typing import List

class ShotMetrics(BaseModel):
    release_height: float
    release_velocity: float
    rhythm_ms: int
    is_consistent: bool
