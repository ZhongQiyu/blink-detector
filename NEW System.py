

import time
import threading
import cv2
import mediapipe as mp
import tkinter as tk
from PIL import Image, ImageTk
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener, Key

class EyeTrackingApp:
    def __init__(self, window_title):
        self.root = tk.Tk()
        self.root.state('zoomed')
        self.root.title(window_title)
        self.root.configure(bg='white')

        top_frame = tk.Frame(self.root, bg='white')
        top_frame.pack(side=tk.TOP, fill=tk.X)

        self.btn_start = tk.Button(top_frame, text="Start", width=20, command=self.start_eye_tracking)
        self.btn_start.pack(pady=10, expand=True)

        self.overlay_frame = tk.Frame(self.root, bg='white', borderwidth=0, highlightthickness=0)
        self.overlay_frame.pack(side=tk.TOP, fill=tk.X, padx=0, pady=10)

        top_row_frame = tk.Frame(self.overlay_frame, bg='white')
        top_row_frame.pack(fill=tk.X)

        self.total_time_count = 0
        self.total_time_elapsed = tk.Label(top_row_frame, text="Total Time Elapsed: 0", font=("Arial", 20), fg='black', bg='white')
        self.total_time_elapsed.pack(side=tk.LEFT, padx=10)
        self.change_total_time_count()

        strictness_frame = tk.Frame(top_row_frame, bg='white')
        strictness_frame.pack(side=tk.LEFT, padx=10)

        self.strictness_value = tk.Label(strictness_frame, font=("Arial", 20), text="Strictness: 0", fg='black', bg='white')
        self.strictness_value.pack(side=tk.LEFT, padx=10)

        self.strictness_textbox = tk.Text(strictness_frame, font=("Arial", 20), height=1, width=5)
        self.strictness_textbox.pack(side=tk.LEFT, padx=10)

        self.set_strictness_button = tk.Button(strictness_frame, text="Set Strictness", font=("Arial", 20), command=self.set_strictness)
        self.set_strictness_button.pack(side=tk.LEFT, padx=10)

        self.warning_msg = tk.Label(strictness_frame, text="", font=("Arial", 15), fg='red', bg='white')
        self.warning_msg.pack(side=tk.LEFT, padx=10)

        new_row_frame = tk.Frame(self.overlay_frame, bg='white')
        new_row_frame.pack(fill=tk.X)

        self.total_blink_count = tk.Label(new_row_frame, text="Total Blink Count: 0", font=("Arial", 20), fg='black', bg='white')
        self.total_blink_count.pack(side=tk.LEFT, padx=10)

        self.total_click_amount = 0
        self.total_clicks = tk.Label(new_row_frame, text="Total Clicks: 0", font=("Arial", 20), fg='black', bg='white')
        self.total_clicks.pack(side=tk.LEFT, padx=10)

        # New Row for Total Keystroke Count
        keystroke_row_frame = tk.Frame(self.overlay_frame, bg='white')
        keystroke_row_frame.pack(fill=tk.X)

        self.total_keystroke_count = 0
        self.total_keystrokes_label = tk.Label(keystroke_row_frame, text="Total Keystroke Count: 0", font=("Arial", 20), fg='black', bg='white')
        self.total_keystrokes_label.pack(side=tk.LEFT, padx=10)

        mouse_thread = threading.Thread(target=self.run_mouse_listener)
        mouse_thread.daemon = True  # Daemon threads exit when the program does
        mouse_thread.start()

        keyboard_thread = threading.Thread(target=self.run_keyboard_listener)
        keyboard_thread.daemon = True
        keyboard_thread.start()

        self.canvas_video = tk.Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight(), bg='white')
        self.canvas_video.pack(fill="both", expand=True)

        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.is_tracking = False
        self.video_source = 0
        self.vid = cv2.VideoCapture(self.video_source)

        self.delay = 15
        self.update()
        self.root.mainloop()

    def change_total_time_count(self):
        self.total_time_elapsed.config(text=f"Total Time Elapsed: {self.total_time_count}")
        self.total_time_count += 1
        self.root.after(1000, self.change_total_time_count)

    def start_eye_tracking(self):
        if not self.is_tracking:
            self.is_tracking = True
            self.btn_start.config(text="Stop")
            self.overlay_frame.lift()
            self.canvas_video.configure(bg='black')
        else:
            self.is_tracking = False
            self.btn_start.config(text="Start")
            self.clear_video_feed()

    def clear_video_feed(self):
        self.canvas_video.delete("all")
        self.canvas_video.configure(bg='white')
        self.canvas_video.create_text(
            self.canvas_video.winfo_width() // 2, self.canvas_video.winfo_height() // 2,
            text="Video feed stopped", font=("Arial", 20), fill="black"
        )

    def update(self):
        ret, frame = self.vid.read()
        if ret and self.is_tracking:
            frame = cv2.flip(frame, 1)
            scaled_frame = cv2.resize(frame, (self.canvas_video.winfo_width(), self.canvas_video.winfo_height()))
            frame_with_eyes = self.detect_eyes(scaled_frame)
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame_with_eyes, cv2.COLOR_BGR2RGB)))
            self.canvas_video.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.root.after(self.delay, self.update)

    def detect_eyes(self, frame):
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(image)
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                eye_indices = list(range(130, 160)) + list(range(385, 398))
                for idx in eye_indices:
                    if idx < len(face_landmarks.landmark):
                        point = face_landmarks.landmark[idx]
                        x = int(point.x * frame.shape[1])
                        y = int(point.y * frame.shape[0])
                        cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
        return frame

    def set_strictness(self):
        value = self.strictness_textbox.get("1.0", "end").strip()
        try:
            intvalue = int(value)
            if 0 <= intvalue <= 75:
                self.strictness_value.config(text="Strictness: " + str(intvalue))
                self.warning_msg.config(text="")
            else:
                self.warning_msg.config(text="Invalid Input! Please enter a number between 0 and 75!")
        except ValueError:
            self.warning_msg.config(text="Invalid Input! Please enter a number!")

    def on_click(self, x, y, button, pressed):
        if pressed:
            self.total_click_amount += 1
            self.update_click_count()

    def update_click_count(self):
        self.total_clicks.config(text="Total Clicks: " + str(self.total_click_amount))

    def on_press(self, key):
        self.total_keystroke_count += 1
        self.update_keystroke_count()

    def update_keystroke_count(self):
        self.total_keystrokes_label.config(text="Total Keystroke Count: " + str(self.total_keystroke_count))
    def run_mouse_listener(self):
        with MouseListener(on_click=self.on_click) as listener:
            listener.join()

    # Separate method to run the keyboard listener
    def run_keyboard_listener(self):
        with KeyboardListener(on_press=self.on_press) as listener:
            listener.join()
    

app = EyeTrackingApp("MediaPipe Eye Tracking with Tkinter")

