import cv2
import numpy as np
import dlib

class EyeTracker:
    def __init__(self, config):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor('models/shape_predictor_68_face_landmarks.dat')
        self.EAR_THRESHOLD = config.get('ear_threshold', 0.2)  # 从配置中获取阈值
        self.blinks = 0

    def track(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.detector(gray)
        blink_detected = False
        for face in faces:
            landmarks = self.predictor(gray, face)

            # 假设左眼是36到41的标记点，右眼是42到47的标记点
            for n in range(36, 48):
                x = landmarks.part(n).x
                y = landmarks.part(n).y
                cv2.circle(frame, (x, y), 2, (255, 0, 0), -1)  # 在眼睛特征点上画红色圆点

            left_eye = self._get_eye(landmarks, 36, 41)
            right_eye = self._get_eye(landmarks, 42, 47)

            left_ear = self._calculate_ear(left_eye)
            right_ear = self._calculate_ear(right_eye)
            ear = (left_ear + right_ear) / 2.0

            if ear < self.EAR_THRESHOLD:
                blink_detected = True
                self.blinks += 1

            frame = self._draw_eye(frame, left_eye)
            frame = self._draw_eye(frame, right_eye)

        return frame, blink_detected

    def _get_eye(self, landmarks, start, end):
        points = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(start, end + 1)]
        return points

    def _draw_eye(self, frame, eye):
        for (x, y) in eye:
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)  # 在眼睛特征点上画绿色圆点
        return frame

    def _analyze_eye(self, eye_points, gray_frame):
        # 这里是一些假设的瞳孔检测或眼睛分析的逻辑
        # 例如，计算眼睛区域的平均亮度，这可能帮助判断眼睛是睁开还是闭合
        eye_region = np.array([eye_points], dtype=np.int32)
        mask = np.zeros(gray_frame.shape[:2], dtype=np.uint8)
        cv2.polylines(mask, eye_region, True, 255, 2)
        cv2.fillPoly(mask, eye_region, 255)
        eye_mask = cv2.bitwise_and(gray_frame, gray_frame, mask=mask)

        mean_val = cv2.mean(eye_mask, mask=mask)[0]
        return mean_val

    def _calculate_ear(self, eye_points):
        A = np.linalg.norm(np.array(eye_points[1]) - np.array(eye_points[5]))
        B = np.linalg.norm(np.array(eye_points[2]) - np.array(eye_points[4]))
        C = np.linalg.norm(np.array(eye_points[0]) - np.array(eye_points[3]))
        return (A + B) / (2.0 * C)

