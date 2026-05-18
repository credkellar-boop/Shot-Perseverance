# Shot-Perseverance

[![Shot-Perseverance CI](https://github.com/credkellar-boop/Shot-Perseverance/actions/workflows/python-app.yml/badge.svg)](https://github.com/credkellar-boop/Shot-Perseverance/actions)
[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688.svg?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8.1.78-green.svg?style=flat&logo=opencv&logoColor=white)](https://opencv.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.15-8A2BE2.svg)](https://google.github.io/mediapipe/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg?logo=docker&logoColor=white)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Shot-Perseverance is an advanced, multi-sport computer vision and analytics OS engine designed to track, classify, and analyze athletic performance in real time. Leveraging MediaPipe pose tracking, OpenCV spatial homography, and custom kinematics models, the engine automatically extracts advanced metrics, triggers algorithmic highlights, detects spectacular plays, and syncs analytics logs directly to cloud pipelines.

---

## 🚀 Key Features

* **Multi-Sport Core OS Engine:** Context-aware physics kernels dynamically swap constants and models across multiple sports including Basketball, Soccer, Hockey, Baseball, and UFC.
* **Biomechanical Kinematics:** Computes precise release heights, velocities, trajectory vectors using the Magnus effect, and joint angles directly from tracking arrays.
* **Spatial Projection & Calibration:** Uses perspective transformations and interactive camera hom

├── .github/
│   └── workflows/
│       └── python-app.yml       # CI/CD automated pipeline running pytest tests
├── api/
│   ├── logger.py               # SQLite asynchronous session and tracking logger
│   ├── main.py                 # FastAPI operational app framework & endpoints
│   └── schemas.py              # Pydantic data schemas for analytical validation
├── core/
│   ├── audio_feedback.py       # Pygame-based sound effect engine 
│   ├── audio_spectator.py      # Crowd noise volume threshold and anomaly calculator
│   ├── ball_physics.py         # Physics mapping incorporating spin and Magnus displacements
│   ├── calibration.py          # Interactive point-to-world mapping utility
│   ├── classifier.py           # AI motion state machine (Jump-shots, fast breaks, etc.)
│   ├── defense_ai.py           # Automated rules-engine scoring for complex defensive shifts
│   ├── goal_detector.py        # Vertical plane boundaries validation for targets
│   ├── kernel.py               # Sport-specific property dispatcher and manager
│   ├── kinematics.py           # Multi-joint trigonometric calculation matrix
│   ├── offside_ai.py           # Soccer 3D pitch coordinate offside calculation rule
│   ├── pitch_calibration.py    # FIFA Standard Pitch homography projection matrix
│   ├── playmaking.py           # Dynamic spatial logic tracking for contextual actions (e.g. Alley-oops)
│   ├── pose_estimator.py       # MediaPipe native model abstraction framework 
│   ├── projection.py           # Top-down planar perspective warp matrix mapper
│   ├── report_gen.py           # FPDF2 automated report generator layout engine
│   ├── session_manager.py      # Highlight filtering architecture & AWS S3 cloud synchronization
│   ├── spectacular_logic.py    # Football/Basketball explicit explosive-movement thresholding
│   ├── transition.py           # Dynamic lane tracking and operational efficiency timers
│   └── video_processor.py      # Interpolation engine handling slow-motion cinematic processing
├── models/
│   └── config.yaml             # Global system configurations, FPS constraints, and sport properties
├── .gitignore                  # Optimized Python environment configuration rule-set
├── Dockerfile                  # Multi-stage container file optimized with headless libraries
├── LICENSE                     # Standard repository distribution governance
├── requirements.txt            # System dependency manifest
└── run_test.py                 # Core pytest framework test suite entrypoint
