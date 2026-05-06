# 🏀 Shot-Perseverance OS

![Build Status](https://img.shields.io/github/actions/workflow/status/darionkellar/shot-perseverance/python-app.yml?branch=main&style=for-the-badge&logo=github)
![Python Version](https://img.shields.io/badge/python-3.11+-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Code Style](https://img.shields.io/badge/code%20style-black-000000?style=for-the-badge)
![OpenCV](https://img.shields.io/badge/OpenCV-4.13.0-white?style=for-the-badge&logo=opencv)

**Shot-Perseverance OS** is a high-performance computer vision engine built for real-time multi-sport analytics. By combining **MediaPipe Pose Estimation** with a custom **Physics Kernel**, the system tracks biomechanics, calculates trajectories, and generates automated highlight reels in 4K.

---

### 🏟 Multi-Sport Kernel Support
The engine dynamically swaps physics constants ($gravity, friction, drag$) and rule-based logic modules:

* **Basketball:** Analyzes "The Dip" rhythm, release height/angle, and detects Alley-oop completion.
* **Soccer (Football):** Real-time offside line visualization and "Beckham Curve" (Magnus effect) prediction.
* **American Football (NFL):** Sack clocks, "Coverage Bubbles" for defensive backs, and yardage tracking.
* **Combat (UFC):** Impact frame analysis, strike velocity, and contact dynamics.
* **Hockey & Baseball:** High-speed object tracking (Puck/Ball) with homography-based velocity scaling.

---

### ✨ Key Features
* **🎬 Cinematic Renderer:** Automated 4K crop-and-zoom on "Spectacular" plays using hip-midpoint tracking.
* **🚀 Spectacular Logic:** Auto-triggers highlight saves based on vertical jump (>30"), ball velocity, or crowd noise decibel spikes.
* **🔊 Audio Intelligence:** Real-time auditory feedback (e.g., "Swish" or "Off-rhythm" cues) via `Pygame` for performance training.
* **☁️ Cloud Sync:** Native AWS S3 integration for automated scouting report and highlight uploads.
* **🛡 Crash Recovery:** "Auto-Heartbeat" system ensures session data is saved to SQLite even during hardware reboots.

---

### 📂 Directory Structure
```text
├── api/             # FastAPI backend for remote logging & schemas
├── core/            # AI Logic: Physics, Kinematics, & Goal Detection
├── github/          # CI/CD workflows for automated testing
├── models/          # YAML configs for sport-specific thresholds
└── Dockerfile       # Production-ready containerization
