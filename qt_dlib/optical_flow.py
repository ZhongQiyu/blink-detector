import cv2
import numpy as np

class EyeTracker:
    def __init__(self):
        self.lk_params = dict(winSize=(15, 15), maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
        self.feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)
        self.track_points = None
        self.old_gray = None

    def detect_features(self, gray):
        self.track_points = cv2.goodFeaturesToTrack(gray, mask=None, **self.feature_params)

    def track_movement(self, gray):
        if self.track_points is not None:
            new_points, status, error = cv2.calcOpticalFlowPyrLK(self.old_gray, gray, self.track_points, None, **self.lk_params)
            good_new = new_points[status == 1]
            good_old = self.track_points[status == 1]
            self.track_points = good_new.reshape(-1, 1, 2)
        self.old_gray = gray.copy()

    def process_frame(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if self.track_points is None:
            self.detect_features(gray)
        else:
            self.track_movement(gray)
            for pt in self.track_points:
                cv2.circle(frame, (pt[0][0], pt[0][1]), 3, (255, 0, 0), -1)

def main():
    cap = cv2.VideoCapture(0)
    eye_tracker = EyeTracker()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        eye_tracker.process_frame(frame)
        cv2.imshow('Eye Tracking', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
