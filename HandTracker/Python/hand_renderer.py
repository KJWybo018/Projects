import cv2

class HandRenderer:
  FINGER_CONNECTIONS = [
        (0, 1), (1, 2), (2, 3), (3, 4),
        (0, 5), (5, 6), (6, 7), (7, 8),
        (0, 9), (9, 10), (10, 11), (11, 12),
        (0, 13), (13, 14), (14, 15), (15, 16),
        (0, 17), (17, 18), (18, 19), (19, 20)
  ]

  def draw(self, frame, landmark_model):
    pts = landmark_model.points

    for a, b in self.FINGER_CONNECTIONS:
      cv2.line(frame, pts[a], pts[b], (0, 255, 0), 2)

    for p in pts:
      cv2.circle(frame, p, 4, (0, 0, 255), -1)

    return frame
