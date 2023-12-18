"""
import cv2

def detect_faces(frame, face_cascade):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return frame

def main():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = detect_faces(frame, face_cascade)
        cv2.imshow('Face Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
"""



"""
import cv2

def detect_and_display(frame, face_cascade, eye_cascade, nose_cascade, mouth_cascade):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 检测脸部
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # 在脸部区域检测眼睛
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 4)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

        # 在脸部区域检测鼻子
        nose = nose_cascade.detectMultiScale(roi_gray, 1.1, 4)
        for (nx, ny, nw, nh) in nose:
            cv2.rectangle(roi_color, (nx, ny), (nx+nw, ny+nh), (0, 255, 255), 2)

        # 在脸部区域检测嘴巴
        mouth = mouth_cascade.detectMultiScale(roi_gray, 1.1, 4)
        for (mx, my, mw, mh) in mouth:
            cv2.rectangle(roi_color, (mx, my), (mx+mw, my+mh), (255, 0, 255), 2)

    cv2.imshow('Face detection', frame)

# 加载 Haar 级联文件
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
nose_cascade = cv2.CascadeClassifier('Nose.xml')  # 需要下载适当的文件
mouth_cascade = cv2.CascadeClassifier('Mouth.xml')  # 需要下载适当的文件

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detect_and_display(frame, face_cascade, eye_cascade, nose_cascade, mouth_cascade)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
"""

import cv2
import mediapipe as mp

# 初始化 MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

# 打开摄像头
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        continue

    # 将 BGR 图像转换为 RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 处理图像并获取面部特征点
    results = face_mesh.process(image)

    # 将图像转换回 BGR 以便显示
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # 绘制面部特征点
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(
                image=image,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_CONTOURS,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp.solutions.drawing_styles
                    .get_default_face_mesh_contours_style())

    # 显示图像
    cv2.imshow('MediaPipe FaceMesh', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
