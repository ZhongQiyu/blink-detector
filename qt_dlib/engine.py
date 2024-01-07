import turtle
import tkinter as tk
import cv2
import time

#t = turtle.Turtle()

class myGui():

    """
    Constructor
    """ 
    def __init__(self):
        self.root = tk.Tk()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.title("AI Timetracker") # program title
        self.root.resizable(True, True)
        self.root.resizable(True, True)

        self.title_txt = tk.Label(self.root, text = "AI Timer", font = ("Arial", 20)) # program window, at the top
        self.title_txt.pack()

        self.make_drag_bar(screen_width)


        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.strictness_textbox = tk.Text(self.frame, font=("Arial", 20), height = 1, width = 5)
        self.button = tk.Button(self.frame, text="Set Strictness", font=("Arial", 20), command = self.onclick_updateBarText)
        self.strictness_textbox.grid(row=0, column=0)
        self.button.grid(row=0, column=1)

        self.bar_text = tk.Label(self.root, text = "Max blink count (Strictness): 0", font = ("Arial", 20))
        self.bar_text.pack()

        self.total_time_elapsed = tk.Label(self.root, text = "Total Time Elapsed: 0", font = ("Arial", 20))
        self.total_time_elapsed.pack()
        self.total_time_count = 0
        self.change_total_time_count()

        self.total_blink_count = tk.Label(self.root, text = "Total Blink Count: 0", font = ("Arial", 20))
        self.total_blink_count.pack()

        self.average_blink_rate = tk.Label(self.root, text = "Average Blink Rate: 0", font = ("Arial", 20))
        self.average_blink_rate.pack()

        self.alarm = tk.Label(self.root, text = "You need a break!", font = ("Arial", 30))
        #self.alarm.pack()

        self.root.mainloop()

    """
    Drag Bar
    """ 
    def make_drag_bar(self, screen_width):
        canvas_width = screen_width * 0.8  # Adjust the canvas width to be 80% of the screen width
        canvas_height = 100  # Keep the canvas height fixed or adjust as needed
        self.canvas = tk.Canvas(self.root, width=canvas_width, height=canvas_height)
        self.canvas.pack()

        self.bar_start = 50
        self.bar_end = canvas_width - 50  # Dynamically set the end of the bar
        self.bar_top = 50
        self.bar_bottom = 50

        # Create a bar on the canvas
        self.canvas.create_line(self.bar_start, self.bar_top, self.bar_end, self.bar_bottom, width=10)
        # Define circle size
        self.circle_radius = 10
        # Adjust the initial position of the circle to be at the edge of the bar
        circle_x = self.bar_start + self.circle_radius
        # Create a circle on the bar
        self.circle = self.canvas.create_oval(circle_x - self.circle_radius, 40, circle_x + self.circle_radius, 60, fill='blue')
        # Bind mouse events to the circle
        self.canvas.tag_bind(self.circle, "<ButtonPress-1>", self.on_drag_start)
        self.canvas.tag_bind(self.circle, "<B1-Motion>", self.on_drag_motion)

    def on_drag_start(self, event):
        # Record the item and its location
        self.drag_data = {"x": event.x, "y": event.y, "item": self.circle}

    def on_drag_motion(self, event):
        # Compute the new position based on the mouse x-coordinate
        new_x1 = event.x - self.circle_radius
        new_x2 = event.x + self.circle_radius
        # Check if the new position is within the bounds of the bar
        if new_x1 >= self.bar_start - self.circle_radius and new_x2 <= self.bar_end + self.circle_radius:
            # Calculate the amount to move
            current_coords = self.canvas.coords(self.drag_data["item"])
            move_x = event.x - (current_coords[0] + self.circle_radius)
            # Move the object the appropriate amount
            self.canvas.move(self.drag_data["item"], move_x, 0)
            # Update the bar text to reflect the new position
            self.updateBarText()

    def onclick_updateBarText(self):
        try:
            count = int(self.strictness_textbox.get("1.0", tk.END).strip())
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            return

        max_count = 75  # Maximum value for strictnesss
        bar_length = self.bar_end - self.bar_start

        if 0 <= count <= max_count:
            scaled_position = (count / max_count) * bar_length
            circle_x = self.bar_start + scaled_position
            self.canvas.coords(self.circle, circle_x - self.circle_radius, 40, circle_x + self.circle_radius, 60)
            self.updateBarText()
        else:
            print(f"Invalid range! Please enter a value between 0 and {max_count}.")

    def updateBarText(self):
        coords = self.canvas.coords(self.circle)
        current_x = (coords[0] + coords[2]) / 2
        max_count = 1500  # Maximum value for the bar count
        bar_length = self.bar_end - self.bar_start
        self.bar_count = ((current_x - self.bar_start) / bar_length) * max_count
        self.bar_text.config(text=f"Max blink count (Strictness): {round(int(self.bar_count) / 20)}")

    """
    Update Total Time Elapsed Function
    """ 
    def change_total_time_count(self):
        self.total_time_elapsed.config(text=f"Total Time Elapsed: {self.total_time_count}")
        self.total_time_count += 1
        self.root.after(1000, self.change_total_time_count) 

my_obj = myGui()

# GUI:
# scale the window to fit your screen (e.g. mine is 2560*1600); can be 1920*1200
# relocate the statistics as a transparent box in top-left/top-right/bottom-left/bottom-right
# design where the buttons and dragger would be (this will be part of my tasks)
from PyQt5 import QtWidgets, QtCore
import sys
import eye_tracking

class Worker(QtCore.QObject):
    updated = QtCore.pyqtSignal(tuple)  # 创建信号，当位置更新时发送

    def run(self):
        self.tracker = eye_tracking.EyeTracker()
        self.tracker.start_tracking()
        while True:
            position = self.tracker.get_current_position()
            self.updated.emit(position)  # 发送信号
            QtCore.QThread.msleep(10)  # 短暂休眠以减少CPU使用

class EyeTrackerUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.worker_thread = QtCore.QThread()  # 创建线程
        self.worker = Worker()  # 创建工作对象
        self.worker.moveToThread(self.worker_thread)  # 将工作对象移动到线程
        self.worker_thread.started.connect(self.worker.run)  # 线程开始时运行run方法
        self.worker.updated.connect(self.update_position)  # 连接更新位置的信号
        self.worker_thread.start()  # 启动线程

    def init_ui(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Eye Tracker')

        self.position_label = QtWidgets.QLabel('Position: (0, 0)', self)
        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.position_label)
        self.setLayout(layout)

        self.show()

    def update_position(self, position):
        self.position_label.setText(f'Position: {position}')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = EyeTrackerUI()
    sys.exit(app.exec_())



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


