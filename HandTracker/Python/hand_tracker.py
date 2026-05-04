import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import os

class HandTracker:
    def __init__(
        self,
        model_path: str = None,
        max_hands: int = 1,
        min_detection_confidence: float = 0.6,
        min_tracking_confidence: float = 0.6
    ):
        if model_path is None:
            # default relative path
            model_path = os.path.join(
                os.path.dirname(__file__),
                "models",
                "hand_landmarker.task"
            )

        base_options = python.BaseOptions(model_asset_path=model_path)
        options = vision.HandLandmarkerOptions(
            base_options=base_options,
            num_hands=max_hands,
            min_hand_detection_confidence=min_detection_confidence,
            min_hand_presence_confidence=min_tracking_confidence,
            min_tracking_confidence=min_tracking_confidence
        )

        self.detector = vision.HandLandmarker.create_from_options(options)

    def detect(self, frame):
        # MediaPipe Tasks expects RGB image in an Image object
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)

        result = self.detector.detect(mp_image)

        # result.hand_landmarks is a list of lists of landmarks
        # We return it in a similar shape to old API: list of hands
        return result.hand_landmarks if result and result.hand_landmarks else None
