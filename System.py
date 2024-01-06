

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

        # Main top frame
        top_frame = tk.Frame(self.root, bg='white')
        top_frame.pack(side=tk.TOP, fill=tk.X)

        self.on_break = False
        self.after_id = None  # Initialize a variable to store the after call ID

        # Center frame for show/hide statistics button and blink count
        center_frame = tk.Frame(top_frame, bg='white')
        center_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.toggle_stats_button = tk.Button(center_frame, text="Show/Hide Statistics", font=("Arial", 20), command=self.toggle_statistics)
        self.toggle_stats_button.pack(pady=10)  # Padding for the button

        # Overlay frame for the left-aligned elements
        self.overlay_frame = tk.Frame(top_frame, bg='white', borderwidth=0, highlightthickness=0)
        self.overlay_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        self.right_side_frame = tk.Frame(top_frame, bg='white')
        self.right_side_frame.pack(side=tk.RIGHT, padx=10, fill=tk.Y)

        # Frame for the total time elapsed
        time_frame = tk.Frame(self.overlay_frame, bg='white')
        time_frame.pack(side=tk.TOP, fill=tk.X, pady=5)

        self.total_time_count = 0
        self.total_time_elapsed = tk.Label(time_frame, text="Total Time Elapsed: 0", font=("Arial", 20), fg='black', bg='white')
        self.total_time_elapsed.pack()
        self.change_total_time_count()

        # Frame for strictness controls
        strictness_frame = tk.Frame(self.overlay_frame, bg='white')
        strictness_frame.pack(side=tk.TOP, fill=tk.X)

        self.strictness = 10
        self.strictness_value = tk.Label(strictness_frame, font=("Arial", 20), text='Strictness: ' + str(self.strictness), fg='black', bg='white')
        self.strictness_value.pack()

        self.strictness_textbox = tk.Text(strictness_frame, font=("Arial", 20), height=1, width=5)
        self.strictness_textbox.pack(pady=(0, 5))  # Reduced padding

        self.set_strictness_button = tk.Button(strictness_frame, text="Set Strictness", font=("Arial", 20), command=self.set_strictness)
        self.set_strictness_button.pack(pady=(0, 5))  # Reduced padding

        self.strictness_explanation = tk.Label(strictness_frame, text="Strictness means the maximum blink count per minute", font=("Arial", 15), fg='black', bg='white')
        self.strictness_explanation.pack() 

        self.warning_msg = tk.Label(strictness_frame, text="", font=("Arial", 15), fg='red', bg='white')
        self.warning_msg.pack()

        # Frame for total blink count
        self.blink_count_frame = tk.Frame(center_frame, bg='white')
        self.blink_count_frame.pack(pady=10)

        self.blink_count = 0
        self.EAR_THRESHOLD = 0.21
        self.eye_closed = False
        self.total_blink_count = tk.Label(self.blink_count_frame, text="Total Blink Count: 0", font=("Arial", 20), fg='black', bg='white')
        self.total_blink_count.pack()

        self.reset_countdown_label = tk.Label(self.blink_count_frame, text="Resets in 60 seconds", font=("Arial", 20), fg='black', bg='white')
        self.reset_countdown_label.pack()
        self.handle_reset_countdown()

        
        self.break_label = tk.Label(center_frame, text="Time for a break!", font=("Arial", 20), fg='red', bg='white')
        self.break_label.pack(pady=10)
        self.break_label.pack_forget()  # This hides the label 

        # Right side frame for clicks and keystrokes
        right_side_frame = tk.Frame(top_frame, bg='white')
        right_side_frame.pack(side=tk.RIGHT, padx=10, fill=tk.Y)

        # Total clicks label (Pack it inside right_side_frame)
        self.total_click_amount = 0
        self.total_clicks = tk.Label(self.right_side_frame, text="Total Clicks: 0", font=("Arial", 20), fg='black', bg='white')
        self.total_clicks.pack(side=tk.TOP, padx=10, fill='x')

        # Total keystrokes label (Pack it inside right_side_frame)
        self.total_keystroke_count = 0
        self.total_keystrokes_label = tk.Label(self.right_side_frame, text="Total Keystroke Count: 0", font=("Arial", 20), fg='black', bg='white')
        self.total_keystrokes_label.pack(side=tk.TOP, padx=10, fill='x')


        mouse_thread = threading.Thread(target=self.run_mouse_listener)
        mouse_thread.daemon = True
        mouse_thread.start()

        keyboard_thread = threading.Thread(target=self.run_keyboard_listener)
        keyboard_thread.daemon = True
        keyboard_thread.start()

        self.canvas_video = tk.Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight(), bg='white')
        self.canvas_video.pack(fill="both", expand=True)

        # Initialize attributes for video capture and face mesh
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.is_tracking = False
        self.video_source = 0
        self.vid = cv2.VideoCapture(self.video_source)
        self.delay = 15

        # Delay the start of video updates until after the mainloop has started
        self.root.after(100, self.start_updates)  # Wait 100ms to allow the window to initialize

        self.root.mainloop()

    def change_total_time_count(self):
        self.total_time_elapsed.config(text=f"Total Time Elapsed: {self.total_time_count}")
        self.total_time_count += 1
        self.root.after(1000, self.change_total_time_count)

    def show_break_label(self):
        self.break_label.pack()

    def hide_break_label(self):
        self.break_label.pack_forget()

    def toggle_statistics(self):
        if self.overlay_frame.winfo_ismapped() and self.right_side_frame.winfo_ismapped() and self.blink_count_frame.winfo_ismapped():
            self.overlay_frame.pack_forget()
            self.right_side_frame.pack_forget()
            self.blink_count_frame.pack_forget()
            self.canvas_video.pack(fill="both", expand=True)
        else:
            self.overlay_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)
            self.blink_count_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
            self.right_side_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10)
            self.canvas_video.pack(fill="both", expand=True)

    def start_eye_tracking(self):
        # Directly start tracking without checking the button state
        self.is_tracking = True
        self.overlay_frame.lift()
        self.canvas_video.configure(bg='black')
    def handle_reset_countdown(self, countdown=60):
        if self.after_id:  # Check if there's an existing after call
            self.root.after_cancel(self.after_id)  # Cancel the previous after call

        if self.on_break:
            if countdown > 0:
                self.reset_countdown_label.config(text=f"Timer stopped, take a break! {countdown} seconds remaining")
                # Store the identifier of the new after call
                self.after_id = self.root.after(1000, self.handle_reset_countdown, countdown - 1)
            else:
                # When break time is over, reset everything
                self.on_break = False
                self.reset_countdown_label.config(text="Resets in 60 seconds")
                self.hide_break_label()
                self.blink_count = 0
                self.total_blink_count.config(text=f"Total Blink Count: {self.blink_count}")
                self.handle_reset_countdown()  # Start the normal countdown
        else:
            if countdown > 0:
                self.reset_countdown_label.config(text=f"Resets in {countdown} seconds")
                # Store the identifier of the new after call
                self.after_id = self.root.after(1000, self.handle_reset_countdown, countdown - 1)
            else:
                # Reset the blink count and restart the countdown when it reaches 0
                self.blink_count = 0
                self.total_blink_count.config(text=f"Total Blink Count: {self.blink_count}")
                self.handle_reset_countdown()  # Reset the countdown



    def clear_video_feed(self):
        self.canvas_video.delete("all")
        self.canvas_video.configure(bg='white')
        self.canvas_video.create_text(
            self.canvas_video.winfo_width() // 2, self.canvas_video.winfo_height() // 2,
            text="Video feed stopped", font=("Arial", 20), fill="black"
        )

    def start_updates(self):
        if not self.is_tracking:
            self.start_eye_tracking()
        self.update()

    def update(self):
        ret, frame = self.vid.read()
        if ret and self.is_tracking:
            frame = cv2.flip(frame, 1)
            canvas_width = self.canvas_video.winfo_width()
            canvas_height = self.canvas_video.winfo_height()

            if canvas_width > 0 and canvas_height > 0:
                frame = self.resize_with_aspect_ratio(frame, width=canvas_width, height=canvas_height)
                if frame is not None:
                    # Process the frame to detect eyes and draw landmarks
                    frame = self.detect_eyes(frame)  # <-- Call detect_eyes here

                    # Convert the frame to a format suitable for Tkinter
                    self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
                    self.canvas_video.create_image((canvas_width - self.photo.width()) // 2, (canvas_height - self.photo.height()) // 2, image=self.photo, anchor=tk.NW)
        self.root.after(self.delay, self.update)


    def resize_with_aspect_ratio(self, image, width=None, height=None, inter=cv2.INTER_AREA):
        (h, w) = image.shape[:2]

        # Calculate the aspect ratio of the image and the desired aspect ratio
        image_aspect = w / h
        desired_aspect = width / height if width is not None and height is not None else image_aspect

        # Calculate scaling factors for resizing the image while maintaining aspect ratio
        if image_aspect > desired_aspect:
            # Image is wider than the desired aspect ratio
            r = width / float(w)
            dim = (width, int(h * r))
        else:
            # Image is taller or equal to the desired aspect ratio
            r = height / float(h)
            dim = (int(w * r), height)

        # Check that dimensions are valid before attempting to resize
        if dim[0] > 0 and dim[1] > 0:
            resized = cv2.resize(image, dim, interpolation=inter)
            return resized
        return None


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
                self.strictness = intvalue
                self.strictness_value.config(text="Strictness: " + str(intvalue))
                self.warning_msg.config(text="")
            else:
                self.warning_msg.config(text="Invalid Input! Please enter a number between 0 and 75!")
        except ValueError:
            self.warning_msg.config(text="Invalid Input! Please enter an integer!")

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

    """
        Eye blink engine time!
    """

    def update_blink_count(self):
        if not self.on_break:  # Only update blink count if not on a break

            # Update the label with the new blink count
            self.total_blink_count.config(text=f"Total Blink Count: {self.blink_count}")

            if self.blink_count >= self.strictness:
                self.show_break_label()
            else:
                self.hide_break_label()

            # Check if the blink count has reached 10 and it's not already on a break
            if self.blink_count >= 10:
                self.initiate_break()

    def initiate_break(self):
        # Set the state to break and update the UI accordingly
        self.on_break = True
        self.show_break_label()
        self.reset_countdown_label.config(text="Timer stopped, take a break!")  # Update the countdown label
        self.handle_reset_countdown(30)  # Start a 30-second break countdown



    def detect_eyes(self, frame):
        # Convert the frame to RGB for MediaPipe processing
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(image)

        # Check if any face landmarks were detected
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # Hypothetical indices for the landmarks of each eye.
                # You need to replace these with the correct indices from MediaPipe
                right_eye_indices = [33, 160, 158, 133, 153, 144]  # replace with the correct indices
                left_eye_indices = [362, 385, 387, 263, 373, 380]

                # Extract the landmark coordinates for each eye
                right_eye = [face_landmarks.landmark[i] for i in right_eye_indices]
                left_eye = [face_landmarks.landmark[i] for i in left_eye_indices]

                # Calculate EAR for both eyes
                left_ear = self.calculate_ear(left_eye)
                right_ear = self.calculate_ear(right_eye)

                # Average the EAR for both eyes for better stability
                ear = (left_ear + right_ear) / 2.0

                # Blink detection logic
                if self.eye_closed and ear > self.EAR_THRESHOLD:
                    self.blink_count += 1
                    self.update_blink_count()
                    self.eye_closed = False  # Reset the eye closed flag
                elif not self.eye_closed and ear < self.EAR_THRESHOLD:
                    self.eye_closed = True  # Set the eye closed flag

                # Visualize the eye landmarks for debugging purposes
                for idx in right_eye_indices + left_eye_indices:
                    if idx < len(face_landmarks.landmark):
                        point = face_landmarks.landmark[idx]
                        x = int(point.x * frame.shape[1])
                        y = int(point.y * frame.shape[0])
                        cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

        return frame


    def calculate_ear(self, eye):
        # EAR calculation with six points
        P2_P6 = self.distance(eye[1], eye[5])
        P3_P5 = self.distance(eye[2], eye[4])
        P1_P4 = self.distance(eye[0], eye[3])
        ear = (P2_P6 + P3_P5) / (2.0 * P1_P4)
        return ear

    def distance(self, p1, p2):
        # Calculate the Euclidean distance between two points
        x_diff = p2.x - p1.x
        y_diff = p2.y - p1.y
        return (x_diff**2 + y_diff**2)**0.5
    

app = EyeTrackingApp("MediaPipe Eye Tracking with Tkinter")



