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



# 11/15:

# 1. What is pynput used for along with the AI module; fix messy code
# 2. How can we set up the AI engine so that it becomes something usable
# 3. Whether I should extend the course or not

# 1.
# - trace: mouse or key
# - mouse, on_move, on_click and on_scroll
# - key, on_press and on_release
# - Q: why we are tracing either or both? if so, then is that a AND or an OR
# - A: sth is missing

# 2. TBA

# 3.
# - Lesson 14 - MESSAGE Marisabel
# - Arrange The Classes
# - Final Goal: Report an APP
# - Final Goal:



# 12/1:

# 1. Compress the class files in HS Project
# 2. Create GitHub repos for HS Project and Python 3 (PyGame); Python 1 if needed; Individual Project PENDING
# 3. Contact Marisabel about extension in HS Project
# 4. Compile an own version of the running project in HS Project
# 5. Compile HW for all classes

# 12/2:

# 12/3:

# 12/4:

# 12/5:

# 1. Create an HTML for demoing the APP using Google Site

# 12/6:

# 1. Sync the whole not just the eyes_rest-main repository with the GitHub token
# 2. Info-hide the project if needed

# 12/7:
