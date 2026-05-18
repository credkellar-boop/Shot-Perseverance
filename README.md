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


---



## Shot-Perseverance/
│
├── .github/
│   └── workflows/
│       └── python-app.yml          # Automated CI/CD Testing Pipeline
│
├── api/                            # HTTP Routing & Data Logging Layer
│   ├── logger.py                   # Async SQLite Database Interaction
│   ├── main.py                     # FastAPI Core App & Endpoint Routing
│   └── schemas.py                  # Pydantic Structural Validation Schemas
│
├── core/                           # Modular OS Analytics Engine
│   │
│   ├── 👁️ CV & Spatial Analytics
│   │   ├── pose_estimator.py       # MediaPipe Tracking Extraction Engine
│   │   ├── calibration.py          # Interactive Pixel-to-World Workspace
│   │   ├── pitch_calibration.py    # Field Homography Mapping Models
│   │   └── projection.py           # Top-Down Perspective Transformation Matrix
│   │
│   ├── 📐 Physics & Kinematics
│   │   ├── ball_physics.py         # Spin, Arc, & Magnus Effect Tracking
│   │   └── kinematics.py           # Angular & Velocity Biomechanical Calculations
│   │
│   ├── 🧠 Game State & Sport AI
│   │   ├── kernel.py               # Dynamic Multi-Sport Property Dispatcher
│   │   ├── classifier.py           # Real-Time Event State Machine
│   │   ├── defense_ai.py           # Defensive Shift & Pressure Evaluation
│   │   ├── goal_detector.py        # Plane/Boundary Intersection Validator
│   │   ├── offside_ai.py           # Positional Offside Evaluation Matrix
│   │   ├── playmaking.py           # Assist & Spatial Chemistry Tracking
│   │   ├── spectacular_logic.py    # Highlight Threshold Rule Logic
│   │   └── transition.py           # Breakaways & Counter-Attack Metrics
│   │
│   └── 🎬 Media, Audio & Reporting
│       ├── audio_feedback.py       # Pygame Low-Latency Audio Event Engine
│       ├── audio_spectator.py      # Spectator Ambient Decibel Thresholding
│       ├── video_processor.py      # Cinematic Framing & Interpolation Engine
│       ├── report_gen.py           # PDF Export Layout & Performance Charts
│       └── session_manager.py      # AWS Cloud Sync & Highlight Filtering
│
├── models/
│   └── config.yaml                 # Global System Thresholds & Constant Rules
│
├── .gitignore                      # Python/VSCode Environment Exclusions
├── Dockerfile                      # Multistage Headless Production Environment
├── LICENSE                         # Repository Legal/Distribution Framework
├── README.md                       # Comprehensive Project Documentation
├── requirements.txt                # Fixed Version Dependency Manifest
└── run_test.py                     # Core Integration & Framework Test Suite
