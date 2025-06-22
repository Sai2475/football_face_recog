# ⚽ Face-The-Pitch: AI Football Player Detector

**Face-The-Pitch** is an AI-powered web application that identifies professional football players from uploaded images. It combines computer vision and large language models to detect faces and retrieve detailed player information such as name, nationality, club, position, and achievements.

---

## 🧠 How It Works

1. **Upload an image** – The user uploads an image of a football player.
2. **Face Detection** – OpenCV's Haar Cascade detects the player's face.
3. **AI Recognition** – The image is sent to a powerful LLaMA 4 model hosted on Groq API.
4. **Player Identification** – The model analyzes the face and returns structured player details.
5. **Output Display** – The detected image and player info are shown on a sleek football-themed UI.

---

## 🔧 Tech Stack

- **Frontend:** HTML, TailwindCSS
- **Backend:** Python, Flask
- **AI Integration:** LLaMA 4 via Groq API
- **Computer Vision:** OpenCV

---

## 📦 Features

- 🧠 LLM-powered football player recognition
- 👤 Accurate face detection using OpenCV
- 🌐 Web-based interface for uploading and displaying results
- 🎨 Stylish, responsive football-themed design
- 🚀 Easily extensible for other sports (e.g., F1, Cricket, NBA)

---
