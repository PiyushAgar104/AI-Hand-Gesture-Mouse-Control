AI Hand Gesture Mouse Control

A real-time AI-based virtual mouse that allows users to control their computer mouse using hand gestures through a webcam.

The project uses OpenCV for video processing, MediaPipe for hand tracking, and PyAutoGUI for controlling the system mouse.

Features
Real-time hand tracking
Smooth mouse cursor movement
Index finger based cursor control
Pinch gesture for left click
Double pinch for double click and opening files/apps
Two-finger gesture for right click
Webcam-based interaction
No physical mouse required
Gesture Controls
Gesture	Action
☝️ Index Finger	Move Cursor
🤏 Index + Thumb Pinch	Left Click
🤏 → Release → 🤏	Double Click / Open
✌️ Index + Middle Finger	Right Click
Q	Exit
Technologies Used
Python
OpenCV
MediaPipe
PyAutoGUI
Computer Vision
Hand Gesture Recognition
Installation

Clone the repository:

git clone https://github.com/your-username/ai-hand-mouse-control.git
cd ai-hand-mouse-control

Install the required libraries:

pip install opencv-python mediapipe pyautogui
Run the Project
python main.py

Allow camera access when requested.

Once the camera window opens:

Show your hand in front of the webcam.
Move your index finger to control the cursor.
Pinch your index finger and thumb to click.
Perform two separate pinches quickly to double-click.
Raise index and middle fingers to perform a right-click.
Press Q to close the application.
How It Works
Webcam
   ↓
OpenCV
   ↓
MediaPipe Hand Detection
   ↓
Hand Landmark Tracking
   ↓
Gesture Recognition
   ↓
PyAutoGUI
   ↓
Mouse Control

MediaPipe detects the hand and tracks 21 hand landmarks. The position of the index finger is mapped to the computer screen coordinates for cursor movement.

The distance between the thumb and index finger is calculated to detect the pinch gesture. Different finger configurations are used to identify left click, double click, and right click actions.

Project Structure
AI-Hand-Mouse-Control/
│
├── main.py
├── README.md
└── requirements.txt
Requirements

Create a requirements.txt file:

opencv-python
mediapipe
pyautogui

Then install everything using:

pip install -r requirements.txt
Future Improvements
Scroll control using hand gestures
Drag and drop gesture
Volume control
Brightness control
Media player controls
Custom gesture configuration
Multi-hand support
Voice + gesture control
Better adaptive cursor smoothing
Use Cases
Touchless computer interaction
Accessibility
Smart interfaces
Human-computer interaction
Computer vision demonstrations
College AI/ML projects
Gesture-based automation
Author

Piyush Agar

B.Tech AI & Data Science
