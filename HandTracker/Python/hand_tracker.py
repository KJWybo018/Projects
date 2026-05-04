import mediapipe as mp
import cv2

class HandTracker:
  def __init__(self, max_hands=1, detection_conf=0.6, tracking_conf=0.6):
    self.mp_hands = mp.solutions.hands
    self.model = self.mp_hands.Hands(
            max_num_hands=max_hands,
            min_detection_confidence=detection_conf,
            min_tracking_confidence=tracking_conf
        )

  def detect(self, frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = self.model.process(rgb)
    return result.multi_hand_landmarks
