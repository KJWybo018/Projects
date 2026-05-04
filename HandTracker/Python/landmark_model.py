class LandmarkModel:
  def __init__(self, raw_landmarks, image_shape):
    self.raw = raw_landmarks
    self.h, self.w = image_shape[:2]
    self.points = self._to_pixel_coords()

  def _to_pixel_coords(self):
    pts = []
    for lm in self.raw.landmark:
      x = int(lm.x * self.w)
      y = int(lm.y * self.h)
      pts.append((x, y))
    return pts
