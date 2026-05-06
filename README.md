# 🏀 Shot-Perseverance: AI-Driven Kinetic Shot Analytics

**Shot-Perseverance** is a high-performance computer vision engine designed to quantify the "un-trackable" elements of a basketball shot. Built for coaches, scouts, and elite players, it uses pose estimation and parabolic trajectory modeling to deliver real-time metrics on player mechanics.

## 🚀 Key Metrics Tracked
* **Release Height:** Precise vertical coordinate of the ball at the moment of detachment.
* **Shot Rhythm:** The "dip-to-release" timing (milliseconds) to measure fluid motion.
* **Release Speed:** The velocity of the ball at the point of exit from the hand.
* **Form Consistency:** Comparative analysis across multiple shots to track mechanical fatigue.

---

## 🛠 Tech Stack
* **Inference:** YOLOv8 / MediaPipe (Skeletal Tracking)
* **Processing:** OpenCV (Asynchronous Frame Analysis)
* **Math Engine:** NumPy / SciPy (Trajectory Arc & Velocity Calculation)
* **API Layer:** FastAPI (High-throughput data delivery)

---

## 🏗 Installation & Usage

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/shot-perseverance.git](https://github.com/your-username/shot-perseverance.git)
cd shot-perseverance
