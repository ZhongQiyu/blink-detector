# answers.py

import cv2
import mediapipe as mp

# 初始化 MediaPipe 面部识别
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# 读取图像文件
image = cv2.imread('path_to_your_image.jpg')

# 转换颜色空间（MediaPipe 需要 RGB 格式）
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 使用 MediaPipe 进行面部识别
with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
    # 处理图像并进行面部识别
    results = face_detection.process(image_rgb)

    # 绘制检测到的面部
    if results.detections:
        for detection in results.detections:
            mp_drawing.draw_detection(image, detection)

# 显示结果
cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()



import cv2
import mediapipe as mp

# 初始化 MediaPipe 解决方案
mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

# 创建一个视频捕捉对象
cap = cv2.VideoCapture(0)

# 使用 Face Mesh
with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as face_mesh:

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue

        # 转换图像颜色空间
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image)

        # 转换回 BGR 用于显示
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # 绘制面部网格
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing.styles
                    .get_default_face_mesh_contours_style())

                # 获取左眼和右眼的关键点
                left_eye = [face_landmarks.landmark[i] for i in range(362, 382)]
                right_eye = [face_landmarks.landmark[i] for i in range(133, 153)]

                # 可以进一步处理这些关键点来追踪眼动

        # 显示图像
        cv2.imshow('MediaPipe Eye Tracking', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
