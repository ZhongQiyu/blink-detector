# Project Workspace

# 12/2:

# Task 0. Eye-Tracking and Anomaly Detection

# - OpenCV
#   - Read the Introduction of OpenCV library in Python (or C++) up to Image Resizing with OpenCV:
#   - https://learnopencv.com/getting-started-with-opencv/. Leave comments for the parts where you do not understand.
#   - Compare the ideas of the basic 'processing' routines we have covered so far. Are they similar? If not, what makes you get around so?

import cv2 
import mediapipe as mp
import numpy as np
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# STEP 1: Read the image as an Object.
img = cv2.imread("C:\\Users\\Cyber\\Pictures\\Camera Roll\\WIN_20231202_14_46_33_Pro.jpg", 1)
model_path = ("C:\\Users\\Cyber\\Desktop\\Python CV2\\efficientdet_lite0.tflite")

# STEP 2: Create an ObjectDetector object.
base_options = python.BaseOptions(model_asset_path='efficientdet.tflite')
options = vision.ObjectDetectorOptions(base_options=base_options,
                                       score_threshold=0.5)
detector = vision.ObjectDetector.create_from_options(options)

# STEP 3: Load the input image.
image = mp.Image.create_from_file(img)

# STEP 4: Detect objects in the input image.
detection_result = detector.detect(image)

# STEP 5: Process the detection result. In this case, visualize it.
image_copy = np.copy(image.numpy_view())
annotated_image = vision.visualize(image_copy, detection_result)
rgb_annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
cv2.imshow(rgb_annotated_image)



# - MediaPipe
#   - Take a picture of your own. Change the format as if you need to.
#   - Use cv2.imread, face_detection and drawing_utils in mediapipe.solutions to detect your face.



#   - Interpret the results. How is the image processed? What does each parameter in the detection method do? How good a result would be?
#   - *Can we have a better result by changing our parameters?











# Task 1. User Interaction:

# - libraries: tkinter and pynput
#   - The event-oriented programming toolset, assmimilating JavaScript's DOM parsing
#   - Inherit the positions from the data provided within Python's scope

# Task 1: GUI Design and Control w/ turtle
# - Draw any shape that assimilates an 3D object.
#   - e.g. it can be a cone, a cube, a pyramid, etc.
#   - Reveal the angle of view as well as you can.
"""


import turtle
from turtle import *

t = Turtle()

def cube(x,y,w):
    ratio = 0.8
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.forward(w)
    t.right(90)
    t.forward(w)
    t.right(90)
    t.forward(w)
    t.right(90)
    t.forward(w)
    t.right(90)
    t.left(45)
    t.forward(w * ratio)
    t.right(45)
    t.forward(w)
    t.right(135)
    t.forward(w * ratio)
    t.right(180)
    t.forward(w * ratio)
    t.right(135)
    t.forward(w)
    t.right(45)
    t.forward(w * ratio) 

"""
# Task 2: GUI Design and Control w/ tk and pynput
# - Build a simple program that allows the user to:
#   - Click on a button that prompts the basic information; parse the information into a list; display the list.
#   - Change the color of the window. The choice of colors can be either user-input or built-in. If user-input, include another button that behaves similarly as the first one does.
#   - Make a timer that records the time since the user runs the program. Before the user shut the program down, display the total amount of time that the program runs in a pop-up window.

# - detect the average frequency for pressing each key
#   - e.g. since the timing session starts, the frequencies are recorded, and the average is taken by frequency/total_time_passed
#   - when the average frequency is larger than a certain self-defined threshold, report the anomaly
#   - when it is the opposite case, report the stability

# - create listeners for both the mouse and the keyboard, and embed the functions into a Python class.
#   - when we invoke the class, would we involve any issue? Why?
#   - print the information of the process for both listeners. give a try.


from pynput import keyboard
# create the diccionary to store the key count

"""

key_counts = ["H", "I"]


def on_press(key):
    try:
        key_str = key.char
    except AttributeError: # like a pcall function in Lua, runs top if no error, runs bottom if top errors. 
        key_str = str(key)

    if key_str in key_counts: 
        key_counts[key_str] += 1 
    else:
        key_counts[key_str] = 1

    print(f"Key pressed: {key_str}, Count: {key_counts[key_str]}")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    # listener.join()
"""


"""
import time
import pynput
from pynput.mouse import Listener   
from pynput import keyboard

class pynput_frequency():
    def __init__(self):
        self.key_dict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.key_data = {}
        for i in self.key_dict:
            self.key_data[i] = 0
        for key in keyboard.Key:
            self.key_data[str(key)] = 0 
        print(self.key_data)
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

    def on_press(self, key):      
        try: 
            key_char = key.char
        except AttributeError:
            key_char = str(key)
        self.key_data[key_char] += 1

class timer():
    def __init__(self):
        self.time = 0
        while True:
            self.change_time()
    def change_time(self):
        self.time += 1
        time.sleep(1)

def calculate_frequency():
    frecuency_obj = pynput_frequency()
    timer_obj = timer()
    time_value = timer_obj.time

#calculate_frequency()



"""