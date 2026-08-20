import cv2
import mediapipe as mp
import pyautogui
import math
import time

SW, SH = pyautogui.size()
pyautogui.PAUSE = 0.01
pyautogui.FAILSAFE = True

mp_hands = mp.solutions.hands
draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75
)

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

sx, sy = SW / 2, SH / 2
smooth = 10
pinch = False
last_click = 0
last_pinch = 0
last_right = 0

while True:
    ok, frame = cap.read()
    if not ok:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    result = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    gesture = "NO HAND"

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]
        draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

        lm = hand.landmark
        thumb, index = lm[4], lm[8]
        middle, ring, pinky = lm[12], lm[16], lm[20]

        d = math.hypot(index.x - thumb.x, index.y - thumb.y)

        iu = index.y < lm[6].y
        mu = middle.y < lm[10].y
        ru = ring.y < lm[14].y
        pu = pinky.y < lm[18].y

        now = time.time()

        if iu and mu and not ru and not pu and d > 0.065:
            gesture = "RIGHT CLICK"
            if now - last_right > 0.8:
                pyautogui.rightClick()
                last_right = now

        elif d < 0.045 and iu:
            gesture = "PINCH"
            if not pinch and now - last_click > 0.35:
                if now - last_pinch < 0.65:
                    pyautogui.doubleClick(interval=0.12)
                    gesture = "DOUBLE CLICK"
                    last_pinch = 0
                else:
                    pyautogui.click()
                    last_pinch = now
                last_click = now
            pinch = True

        elif d > 0.065:
            gesture = "MOVE"
            pinch = False

            tx = index.x * SW
            ty = index.y * SH

            dx, dy = tx - sx, ty - sy

            if abs(dx) > 3:
                sx += dx / smooth
            if abs(dy) > 3:
                sy += dy / smooth

            sx = max(0, min(SW - 1, sx))
            sy = max(0, min(SH - 1, sy))

            pyautogui.moveTo(int(sx), int(sy))

        ix, iy = int(index.x * w), int(index.y * h)
        cv2.circle(frame, (ix, iy), 10, (0, 255, 0), -1)

        if d < 0.045:
            cv2.line(
                frame,
                (ix, iy),
                (int(thumb.x * w), int(thumb.y * h)),
                (0, 255, 0), 4
            )

    cv2.putText(
        frame,
        "Gesture: " + gesture,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    cv2.putText(
        frame,
        "Index=Move | Pinch=Click | Double Pinch=Open | Q=Exit",
        (20, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (255, 255, 255),
        2
    )

    cv2.imshow("AI Hand Mouse Control", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()