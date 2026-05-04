import cv2
from frame_source import FrameSource
from hand_tracker import HandTracker
from landmark_model import LandmarkModel
from hand_renderer import HandRenderer

class HandTrackingApp:
    def __init__(self):
        self.camera = FrameSource()
        self.tracker = HandTracker()
        self.renderer = HandRenderer()

    def run(self):
        while True:
            frame = self.camera.get_frame()
            if frame is None:
                break

            hands = self.tracker.detect(frame)

            if hands:
                for hand_landmarks in hands:
                    lm = LandmarkModel(hand_landmarks, frame.shape)
                    frame = self.renderer.draw(frame, lm)

            cv2.imshow("Hand Tracker", frame)
            if cv2.waitKey(1) == 27:
                break

        self.camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    HandTrackingApp().run()