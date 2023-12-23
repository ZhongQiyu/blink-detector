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

"""
import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()
cap = cv2.VideoCapture(0)

def resize_frame(frame, scale_percent=50):
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        continue

    # 调整图像分辨率
    frame = resize_frame(frame, scale_percent=50)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(
                image=frame,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_CONTOURS,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp.solutions.drawing_styles
                    .get_default_face_mesh_contours_style())

    cv2.imshow('MediaPipe FaceMesh', frame)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
"""

"""
import cv2
import mediapipe as mp
import threading
import queue

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()
cap = cv2.VideoCapture(0)

processed_frame_queue = queue.Queue(maxsize=5)
frame_count = 0
frame_skip = 5
exit_flag = False

def resize_frame(frame, scale_percent=30):  # 减少分辨率以提高性能
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

def process_frames():
    global frame_count, exit_flag
    while not exit_flag:
        ret, frame = cap.read()
        if not ret:
            continue

        frame_count += 1
        if frame_count % frame_skip != 0:
            continue
        
        resized_frame = resize_frame(frame)
        resized_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(resized_frame)
        resized_frame = cv2.cvtColor(resized_frame, cv2.COLOR_RGB2BGR)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(
                    image=resized_frame,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp.solutions.drawing_styles
                        .get_default_face_mesh_contours_style())

        if processed_frame_queue.qsize() < 5:  # 防止队列阻塞
            processed_frame_queue.put(resized_frame)

processing_thread = threading.Thread(target=process_frames)
processing_thread.start()

while not exit_flag:
    if not processed_frame_queue.empty():
        frame_to_display = processed_frame_queue.get()
        cv2.imshow('MediaPipe FaceMesh', frame_to_display)
        if cv2.waitKey(5) & 0xFF == 27:
            exit_flag = True

processing_thread.join()
cap.release()
cv2.destroyAllWindows()
"""



"""
import cv2
import mediapipe as mp
from pynput import keyboard, mouse
import time

# MediaPipe 设置
mp_hands = mp.solutions.hands

# 全局变量
start_time = time.time()
click_count = 0
min_detection_confidence = 0.5

# 键盘监听回调函数
def on_press(key):
    try:
        print(f"Key {key.char} pressed")
    except AttributeError:
        print(f"Special key {key} pressed")

# 鼠标监听回调函数
def on_click(x, y, button, pressed):
    global click_count
    if pressed:
        click_count += 1

# 设置键盘监听
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

# 设置鼠标监听
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

# 打开摄像头
cap = cv2.VideoCapture(0)

# 创建滑块窗口
cv2.namedWindow('MediaPipe Hands')

# 滑块回调函数
def on_trackbar(val):
    global min_detection_confidence
    min_detection_confidence = val / 100

# 添加滑块
cv2.createTrackbar('Confidence', 'MediaPipe Hands', int(min_detection_confidence * 100), 100, on_trackbar)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # 计算流逝的时间
    elapsed_time = int(time.time() - start_time)

    # 处理帧
    frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
    frame.flags.writeable = False

    # 使用滑块更新的参数
    with mp_hands.Hands(min_detection_confidence=min_detection_confidence, min_tracking_confidence=0.5) as hands:
        results = hands.process(frame)

    # 绘制手部标记
    frame.flags.writeable = True
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # 获取视频尺寸
    height, width = frame.shape[:2]

    # 显示流逝的时间和点击次数
    cv2.putText(frame, f"Time: {elapsed_time} s", (width - 220, height - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"Clicks: {click_count}", (width - 220, height - 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('MediaPipe Hands', frame)
    if cv2.waitKey(1) & 0xFF == 27:  # 按 ESC 键退出
        break

cap.release()
cv2.destroyAllWindows()
keyboard_listener.stop()
mouse_listener.stop()
"""



"""
import cv2
import mediapipe as mp
from pynput import keyboard, mouse
import time

# MediaPipe 设置
mp_face_mesh = mp.solutions.face_mesh

# 全局变量
start_time = time.time()
click_count = 0
min_detection_confidence = 0.5

# 键盘监听回调函数
def on_press(key):
    try:
        print(f"Key {key.char} pressed")
    except AttributeError:
        print(f"Special key {key} pressed")

# 鼠标监听回调函数
def on_click(x, y, button, pressed):
    global click_count
    if pressed:
        click_count += 1

# 设置键盘监听
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

# 设置鼠标监听
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

# 打开摄像头
cap = cv2.VideoCapture(0)

# 创建滑块窗口
cv2.namedWindow('MediaPipe Face Mesh')

# 滑块回调函数
def on_trackbar(val):
    global min_detection_confidence
    min_detection_confidence = val / 100

# 添加滑块
cv2.createTrackbar('Confidence', 'MediaPipe Face Mesh', int(min_detection_confidence * 100), 100, on_trackbar)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # 计算流逝的时间
    elapsed_time = int(time.time() - start_time)

    # 处理帧
    frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
    frame.flags.writeable = False

    # 使用滑块更新的参数
    with mp_face_mesh.FaceMesh(min_detection_confidence=min_detection_confidence, min_tracking_confidence=0.5) as face_mesh:
        results = face_mesh.process(frame)

    # 绘制面部标记
    frame.flags.writeable = True
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # 绘制眼睛区域的关键点（选择特定的关键点）
            eye_keypoints_indices = [33, 133, 160, 158, 153, 144, 362, 385, 387, 380, 374, 263]  # 特定的眼睛关键点索引
            for index in eye_keypoints_indices:
                point = face_landmarks.landmark[index]
                x = int(point.x * frame.shape[1])
                y = int(point.y * frame.shape[0])
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

    # 获取视频尺寸
    height, width = frame.shape[:2]

    # 显示流逝的时间和点击次数
    cv2.putText(frame, f"Time: {elapsed_time} s", (width - 220, height - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"Clicks: {click_count}", (width - 220, height - 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('MediaPipe Face Mesh', frame)
    if cv2.waitKey(1) & 0xFF == 27:  # 按 ESC 键退出
        break

cap.release()
cv2.destroyAllWindows()
keyboard_listener.stop()
mouse_listener.stop()
"""



"""
import cv2
import mediapipe as mp
from pynput import keyboard, mouse
import time

# MediaPipe 设置
mp_face_mesh = mp.solutions.face_mesh

# 全局变量
start_time = time.time()
click_count = 0
min_detection_confidence = 0.5
last_key_pressed = "None"

# 键盘监听回调函数
def on_press(key):
    global last_key_pressed
    try:
        last_key_pressed = key.char
    except AttributeError:
        last_key_pressed = str(key)

# 鼠标监听回调函数
def on_click(x, y, button, pressed):
    global click_count
    if pressed:
        click_count += 1

# 设置键盘监听
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

# 设置鼠标监听
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

# 打开摄像头
cap = cv2.VideoCapture(0)

# 创建滑块窗口
cv2.namedWindow('MediaPipe Face Mesh')

# 滑块回调函数
def on_trackbar(val):
    global min_detection_confidence
    min_detection_confidence = val / 100

# 添加滑块
cv2.createTrackbar('Confidence', 'MediaPipe Face Mesh', int(min_detection_confidence * 100), 100, on_trackbar)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # 计算流逝的时间
    elapsed_time = int(time.time() - start_time)

    # 处理帧
    frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
    frame.flags.writeable = False

    # 使用滑块更新的参数
    with mp_face_mesh.FaceMesh(min_detection_confidence=min_detection_confidence, min_tracking_confidence=0.5) as face_mesh:
        results = face_mesh.process(frame)

    # 绘制面部标记
    frame.flags.writeable = True
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # 获取视频尺寸
    height, width = frame.shape[:2]

    # 显示流逝的时间和点击次数
    cv2.putText(frame, f"Time: {elapsed_time} s", (width - 220, height - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"Clicks: {click_count}", (width - 220, height - 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"Last Key: {last_key_pressed}", (width - 220, height - 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('MediaPipe Face Mesh', frame)
    if cv2.waitKey(1) & 0xFF == 27:  # 按 ESC 键退出
        break

cap.release()
cv2.destroyAllWindows()
keyboard_listener.stop()
mouse_listener.stop()
"""



import cv2
import mediapipe as mp
from pynput import keyboard, mouse
import time
import numpy as np

# 定义眼睛长宽比计算函数
def calculate_ear(eye_points):
    # 计算欧式距离的辅助函数
    def euclidean_distance(point_a, point_b):
        return np.sqrt((point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2)

    # 计算垂直距离
    vertical1 = euclidean_distance(eye_points[1], eye_points[5])
    vertical2 = euclidean_distance(eye_points[2], eye_points[4])

    # 计算水平距离
    horizontal = euclidean_distance(eye_points[0], eye_points[3])

    # 计算EAR
    ear = (vertical1 + vertical2) / (2.0 * horizontal)
    return ear

# 设置EAR阈值和连续帧数阈值
EAR_THRESHOLD = 0.2
CONSEC_FRAMES = 2

# MediaPipe 设置
mp_face_mesh = mp.solutions.face_mesh

# 全局变量
start_time = time.time()
click_count = 0
min_detection_confidence = 0.5
last_key_pressed = "None"
blink_count = 0
ear_counter = 0
ear = 0.3  # 初始EAR
eye_points_count = 20  # 初始关键点数量

# 键盘监听回调函数
def on_press(key):
    global last_key_pressed
    try:
        last_key_pressed = key.char
    except AttributeError:
        last_key_pressed = str(key)

# 鼠标监听回调函数
def on_click(x, y, button, pressed):
    global click_count
    if pressed:
        click_count += 1

# 设置键盘监听
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

# 设置鼠标监听
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

# 打开摄像头
cap = cv2.VideoCapture(0)

# 创建滑块窗口
cv2.namedWindow('MediaPipe Face Mesh')

# 滑块回调函数
def on_trackbar_confidence(val):
    global min_detection_confidence
    min_detection_confidence = val / 100

# 添加滑块
cv2.createTrackbar('Confidence', 'MediaPipe Face Mesh', int(min_detection_confidence * 100), 100, on_trackbar_confidence)

# 添加眼部关键点数量调整的滑块
def on_trackbar_eye_points(val):
    global eye_points_count
    eye_points_count = val

cv2.createTrackbar('Eye Points', 'MediaPipe Face Mesh', eye_points_count, 100, on_trackbar_eye_points)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # 计算流逝的时间
    elapsed_time = int(time.time() - start_time)

    # 处理帧
    frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
    frame.flags.writeable = False

    # 使用滑块更新的参数
    with mp_face_mesh.FaceMesh(min_detection_confidence=min_detection_confidence, min_tracking_confidence=0.5) as face_mesh:
        results = face_mesh.process(frame)

    # 绘制面部标记
    frame.flags.writeable = True
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # 获取视频尺寸
    height, width = frame.shape[:2]

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            landmarks = [(lm.x, lm.y) for lm in face_landmarks.landmark]
            
            # 获取左眼和右眼的特征点
            left_eye_points = [(int(lm.x * width), int(lm.y * height)) for lm in face_landmarks.landmark[362:362+eye_points_count]]
            right_eye_points = [(int(lm.x * width), int(lm.y * height)) for lm in face_landmarks.landmark[133:133+eye_points_count]]
            
            # 计算并更新EAR
            left_ear = calculate_ear(left_eye_points)
            right_ear = calculate_ear(right_eye_points)
            ear = (left_ear + right_ear) / 2

            # 检测眨眼
            if ear < EAR_THRESHOLD:
                ear_counter += 1
            else:
                if ear_counter >= CONSEC_FRAMES:
                    blink_count += 1
                ear_counter = 0

            # 绘制眼睛中心（绿色）
            cv2.circle(frame, left_eye_points[8], 2, (0, 255, 0), -1)
            cv2.circle(frame, right_eye_points[8], 2, (0, 255, 0), -1)

            # 绘制眼睛特征点（红色）
            for point in left_eye_points + right_eye_points:
                cv2.circle(frame, point, 1, (0, 0, 255), -1)

    # 在右下角显示信息
    cv2.putText(frame, f"Time: {elapsed_time}s", (width - 220, height - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"Clicks: {click_count}", (width - 220, height - 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"Last Key: {last_key_pressed}", (width - 220, height - 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"Blinks: {blink_count}", (width - 220, height - 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('MediaPipe Face Mesh', frame)
    if cv2.waitKey(1) & 0xFF == 27:  # 按 ESC 键退出
        break

cap.release()
cv2.destroyAllWindows()
keyboard_listener.stop()
mouse_listener.stop()

