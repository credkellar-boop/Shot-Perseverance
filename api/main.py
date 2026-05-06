from fastapi import FastAPI, UploadFile, File
from api.schemas import ShotMetrics
import uvicorn

app = FastAPI(title="Shot-Perseverance API")

@app.post("/analyze-shot", response_model=ShotMetrics)
async def analyze_shot(file: UploadFile = File(...)):
    # 1. Save file to data/raw_videos
    # 2. Call core.video_processor
    # 3. Return calculated metrics
    return {
        "release_height": 9.2,
        "release_velocity": 12.5,
        "rhythm_ms": 450,
        "is_consistent": True
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

