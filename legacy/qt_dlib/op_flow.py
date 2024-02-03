import tkinter as tk
from PIL import Image, ImageTk
import cv2
import threading
from pynput import keyboard, mouse
import mediapipe as mp

class MyGUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Eye and Keyboard/Mouse Tracker with Face Detection")
        self.root.state('zoomed')

        self.is_running = True
        self.cap = cv2.VideoCapture(0)
        self.setup_ui_components()

        # MediaPipe 面部标记配置
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

        # 启动键盘和鼠标监听
        self.start_listeners()

        # 启动视频循环线程
        self.start_video_thread()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def setup_ui_components(self):
        self.video_frame = tk.Canvas(self.root, bg='black')
        self.video_frame.pack(fill='both', expand=True)

        self.lbl_key_data = tk.Label(self.root, text="Key Data: None", font=("Arial", 20), bg="black", fg="white")
        self.lbl_key_data.place(x=20, y=20)

        self.lbl_mouse_data = tk.Label(self.root, text="Mouse Data: None", font=("Arial", 20), bg="black", fg="white")
        self.lbl_mouse_data.place(x=20, y=60)

    def start_video_thread(self):
        threading.Thread(target=self.video_loop, daemon=True).start()

    def start_listeners(self):
        self.keyboard_listener = keyboard.Listener(on_press=self.on_key_press)
        self.mouse_listener = mouse.Listener(on_move=self.on_mouse_move)
        self.keyboard_listener.start()
        self.mouse_listener.start()

    def on_key_press(self, key):
        try:
            key_data = f"Key pressed: {key.char}"
        except AttributeError:
            key_data = f"Special key pressed: {key}"
        self.lbl_key_data.config(text=key_data)

    def on_mouse_move(self, x, y):
        mouse_data = f"Mouse moved to ({x}, {y})"
        self.lbl_mouse_data.config(text=mouse_data)

    def video_loop(self):
        while self.is_running:
            ret, frame = self.cap.read()
            if not ret:
                continue

            try:
                # MediaPipe 处理
                results = self.face_mesh.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                if results.multi_face_landmarks:
                    for face_landmarks in results.multi_face_landmarks:
                        # 这里可以根据需要处理 face_landmarks
                        pass
            except Exception as e:
                print("MediaPipe处理错误:", e)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.video_frame.create_image(0, 0, image=self.photo, anchor=tk.NW)
            self.root.update()

    def on_closing(self):
        self.is_running = False
        if self.cap.isOpened():
            self.cap.release()
        if self.keyboard_listener is not None:
            self.keyboard_listener.stop()
        if self.mouse_listener is not None:
            self.mouse_listener.stop()
        self.root.destroy()

app = MyGUI()
