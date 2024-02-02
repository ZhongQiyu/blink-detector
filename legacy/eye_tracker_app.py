import tkinter as tk
import threading
import cv2
import mediapipe as mp
from PIL import Image, ImageTk
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener, Key

class EyeTrackingApp:
    def __init__(self, window_title):
        # 初始化窗口和布局
        # ...

        # 初始化视频捕获和面部网格
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.is_tracking = False
        self.video_source = 0
        self.vid = cv2.VideoCapture(self.video_source)
        self.delay = 15

        # 初始化鼠标和键盘监听器线程
        mouse_thread = threading.Thread(target=self.run_mouse_listener)
        mouse_thread.daemon = True
        mouse_thread.start()

        keyboard_thread = threading.Thread(target=self.run_keyboard_listener)
        keyboard_thread.daemon = True
        keyboard_thread.start()

        # 启动界面更新循环
        self.root.after(100, self.start_updates)
        self.root.mainloop()

    # 实现其他必要的方法，如 start_eye_tracking, update, detect_eyes 等
    # ...

    def start_updates(self):
        if not self.is_tracking:
            self.start_eye_tracking()
        self.update()

    # 更新视频帧和眨眼检测逻辑
    def update(self):
        # 实现视频帧更新和眨眼检测
        # ...

    def run_mouse_listener(self):
        with MouseListener(on_click=self.on_click) as listener:
            listener.join()

    def run_keyboard_listener(self):
        with KeyboardListener(on_press=self.on_press) as listener:
            listener.join()

    # 实现鼠标点击和键盘敲击的监听方法
    # ...

# 启动应用程序
app = EyeTrackingApp("MediaPipe Eye Tracking with Tkinter")
