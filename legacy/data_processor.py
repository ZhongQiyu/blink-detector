from scipy.spatial import distance as dist

class DataProcessor:
    def __init__(self):
        self.blink_count = 0
        self.eye_positions = []
        self.ear_threshold = 0.2  # EAR阈值，可能需要根据实际情况进行调整
        self.ear_consecutive_frames = 3  # 连续多少帧闭眼则认为是一次眨眼
        self.last_blink_timestamp = None
        self.frame_counter = 0

    def process_data(self, frame, landmarks):
        # 假设landmarks是一个包含所有面部特征点的列表
        left_eye_landmarks = landmarks[36:42]  # 左眼的Dlib标记点
        right_eye_landmarks = landmarks[42:48]  # 右眼的Dlib标记点
        left_eye_position = self._calculate_eye_center(left_eye_landmarks)
        right_eye_position = self._calculate_eye_center(right_eye_landmarks)

        # 存储眼睛位置
        self.eye_positions.append((left_eye_position, right_eye_position))

        # 调用眨眼计数逻辑
        self.count_blinks(left_eye_landmarks, right_eye_landmarks)

    def ear(self, eye):
        # 垂直眼睑的两个距离
        vertical1 = dist.euclidean(eye[1], eye[5])
        vertical2 = dist.euclidean(eye[2], eye[4])

        # 水平眼睑之间的距离
        horizontal = dist.euclidean(eye[0], eye[3])

        # 计算ear值
        ear = (vertical1 + vertical2) / (2.0 * horizontal)
        return ear

    def calculate_ear(self, left_eye, right_eye):
        # 计算两个眼睛的EAR并取平均值
        left_ear = self.ear(left_eye)
        right_ear = self.ear(right_eye)
        ear = (left_ear + right_ear) / 2.0
        return ear

    def current_time(self):
        # 返回当前时间的辅助函数，用于跟踪眨眼时间
        return time.time()

    def _calculate_eye_center(self, eye_landmarks):
        # 基于眼睛的标记点计算眼睛的中心位置
        x_coords = [p.x for p in eye_landmarks]
        y_coords = [p.y for p in eye_landmarks]
        x_center = sum(x_coords) / len(x_coords)
        y_center = sum(y_coords) / len(y_coords)
        return (x_center, y_center)

    def _calculate_eye_aspect_ratio(self, eye_landmarks):
        # 根据6个特定的眼部标记点计算EAR
        # 眼睛标记点的顺序通常是：左上角（1），左中角（2），左下角（3），右下角（4），右中角（5），右上角（6）

        # 计算两组垂直的眼睛标记点之间的距离
        vertical1 = dist.euclidean(eye_landmarks[1], eye_landmarks[5])
        vertical2 = dist.euclidean(eye_landmarks[2], eye_landmarks[4])

        # 计算水平的眼睛标记点之间的距离
        horizontal = dist.euclidean(eye_landmarks[0], eye_landmarks[3])

        # 计算EAR
        ear = (vertical1 + vertical2) / (2.0 * horizontal)
        return ear

    def count_blinks(self, left_eye_landmarks, right_eye_landmarks):
        # 根据眼睛的纵横比计算是否闭眼
        left_eye_ratio = self._calculate_eye_aspect_ratio(left_eye_landmarks)
        right_eye_ratio = self._calculate_eye_aspect_ratio(right_eye_landmarks)

        if left_eye_ratio < self.ear_threshold and right_eye_ratio < self.ear_threshold:
            self.frame_counter += 1
            # 如果连续多帧低于阈值，则认为是一次眨眼
            if self.frame_counter >= self.ear_consecutive_frames:
                self.blink_count += 1
                self.frame_counter = 0
        else:
            self.frame_counter = 0
