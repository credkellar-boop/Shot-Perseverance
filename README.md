# 🏀 Shot-Perseverance OS

![Build Status](https://img.shields.io/github/actions/workflow/status/darionkellar/shot-perseverance/python-app.yml?branch=main&style=for-the-badge)
![Python Version](https://img.shields.io/badge/python-3.11-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Maintained](https://img.shields.io/badge/Maintained%3F-yes-brightgreen?style=for-the-badge)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-orange?style=for-the-badge)

**Shot-Perseverance OS** is a high-performance, multi-sport computer vision engine designed to analyze biomechanics, physics, and tactical play in real-time. By leveraging **Homography Matrices**, **MediaPipe Pose Estimation**, and **Custom Physics Kernels**, it transforms standard 2D video into a rich 4K analytical broadcast.

---

### 🏟 Supported Sports & Logic
The system uses a dynamic `SportKernel` to swap physics constants and rule-based logic modules:

* **Basketball:** Shot tracking (release height/angle), Alley-oop detection, and "The Dip" rhythm analysis.
* **Soccer (Football):** Real-time offside line visualization and "Beckham Curve" trajectory prediction.
* **American Football (NFL):** Sack clocks, "Coverage Bubbles," and yardage gain tracking.
* **Hockey:** High-speed puck tracking with adjusted collision friction.
* **Baseball:** Pitch velocity and ball-9IN contact dynamics.
* **UFC/Combat:** Contact dynamics and strike impact frame analysis.

---

### ✨ Core Features
* **Cinematic Renderer:** Automated 4K crop/zoom on "Spectacular" plays.
* **Spectacular Logic:** Auto-saves highlights based on vertical jump, ball velocity, or crowd noise spikes.
* **Audio Intelligence:** Real-time feedback via `Pygame` for rhythm training and auditory cues.
* **Cloud Sync:** Automated AWS S3 syncing for scouting reports and highlight reels.
* **Auto-Heartbeat:** Resilient session management that survives crashes via local SQLite logging.

---

### 🛠 Installation

1. **Clone & Enter:**
   ```bash
   git clone [https://github.com/darionkellar/shot-perseverance.git](https://github.com/darionkellar/shot-perseverance.git)
   cd shot-perseverance
