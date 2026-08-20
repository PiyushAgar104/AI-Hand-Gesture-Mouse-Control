AI HAND GESTURE CONTROL

Control Your Computer With Just One Hand

AI Hand Mouse is a real-time computer vision project that transforms your webcam into a virtual mouse. Move your cursor, click, right-click, and open applications — all using simple hand gestures.

No mouse. No touch. Just your hand.

🚀 What Can It Do?
🖐️ Gesture	🖥️ Action
☝️ Index Finger	Move Cursor
🤏 Pinch	Left Click
🤏 → Release → 🤏	Double Click / Open
✌️ Index + Middle	Right Click
⌨️ Q	Exit
🧠 How It Works
        📷 Webcam
            │
            ▼
     🔍 OpenCV Processing
            │
            ▼
      ✋ MediaPipe
    Hand Landmark Detection
            │
            ▼
     🧠 Gesture Recognition
            │
            ▼
       🖱️ PyAutoGUI
            │
            ▼
      💻 Mouse Control

The webcam captures your hand in real time.

MediaPipe detects 21 hand landmarks, while the program calculates finger positions and distances to identify gestures.

The index finger position is mapped to your screen coordinates to create smooth cursor movement.

✨ Key Features
🎥 Real-time webcam tracking
✋ 21-point hand landmark detection
🖱️ Touchless mouse control
🎯 Smooth cursor movement
🤏 Pinch-based clicking
🖱️ Right-click gesture
📂 Double-click to open files/apps
⚡ Real-time gesture recognition
🔒 Runs locally on your computer
🛠️ Tech Stack
Python
│
├── OpenCV       → Computer Vision
├── MediaPipe    → Hand Tracking
└── PyAutoGUI    → Mouse Automation
⚙️ Installation
1. Clone the repository
git clone https://github.com/your-username/ai-hand-mouse.git
cd ai-hand-mouse
2. Install dependencies
pip install opencv-python mediapipe pyautogui
3. Run
python main.py

That's it. 🎉

Make sure your webcam is available and visible to the application.

🎮 Quick Demo
Start Camera
     ↓
Show Hand
     ↓
☝️ Move Finger
     ↓
🖱️ Cursor Moves
     ↓
🤏 Pinch
     ↓
🖱️ Click
     ↓
🤏 Release + Pinch
     ↓
📂 Open File / Application
📁 Project Structure
AI-Hand-Mouse/
│
├── main.py
├── requirements.txt
└── README.md
🔮 What's Next?

This project can be extended into a complete AI Gesture Control System.

Future Ideas
🖱️ Drag & Drop
📜 Scroll Up / Down
🔊 Volume Control
💡 Screen Brightness Control
🎵 Media Controls
🔍 Zoom In / Out
✋ Custom User Gestures
🤖 AI Voice + Gesture Control
🖐️ Multi-Hand Interaction
💡 Why This Project?

Traditional mouse interaction requires physical hardware.

This project explores how Computer Vision + AI + Human-Computer Interaction can create a more natural and touchless way to interact with computers.

Your hand becomes the controller.

👨‍💻 Author
Piyush Agar

B.Tech — AI & Data Science

Built with ❤️, Python and Computer Vision.
