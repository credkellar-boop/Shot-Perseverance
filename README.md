# ⚾ Shot-Perseverance OS

![Build Status](https://img.shields.io/github/actions/workflow/status/darionkellar/shot-perseverance/python-app.yml?branch=main&style=for-the-badge&logo=github)
![Python Version](https://img.shields.io/badge/python-3.11+-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

**Shot-Perseverance OS** is a high-performance computer vision engine for real-time multi-sport analytics. It tracks biomechanics, calculates trajectories (using the $Magnus Effect$), and generates automated 4K highlight reels.

---

### 🏟 Multi-Sport Support
* **⚾ Baseball:** Real-time pitch velocity, break-point calculation, and bat-contact dynamics.
* **🏀 Basketball:** "The Dip" rhythm analysis, release height, and Alley-oop detection.
* **⚽ Soccer:** Offside line visualization and "Beckham Curve" prediction.
* **🏈 Football:** Sack clocks and defensive coverage bubbles.
* **🥊 Combat:** Strike velocity and impact frame dynamics.

---

### 🛠 Tech Stack (2026)
| Library | Version | Role |
| :--- | :--- | :--- |
| **OpenCV** | `4.13.0.92` | Vision Engine |
| **MediaPipe** | `0.10.35` | Pose Estimation |
| **NumPy** | `2.4.4` | Physics Math |
| **pytest** | `8.2.0` | CI/CD Testing |

---

### 🚀 Usage
1. `pip install -r requirements.txt`
2. `python main.py`
* **☁️ Cloud Sync:** Native AWS S3 integration for automated scouting report and highlight uploads.
* **🛡 Crash Recovery:** "Auto-Heartbeat" system ensures session data is saved to SQLite even during hardware reboots.

---

### 📂 Directory Structure
```text
├── api/             # FastAPI backend for remote logging & schemas
├── core/            # AI Logic: Physics, Kinematics, & Goal Detection
├── .github/         # CI/CD workflows for automated testing (pytest)
├── models/          # YAML configs for sport-specific thresholds
└── Dockerfile       # Production-ready containerization
