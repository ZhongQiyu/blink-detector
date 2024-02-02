# 11/3-11/4

import tkinter as tk

def on_click(x, y, button, pressed):
    if pressed:
        label.config(text=f"Button {button} pressed at {(x, y)}")

def tk_demo():
    root = tk.Tk()
    label = tk.Label(root, text="Click anywhere!")
    label.pack(pady=20)

    listener = mouse.Listener(on_click=on_click)
    listener.start()
    root.mainloop()
    listener.stop()

# tk_demo()

# The #2 in 1/3 - Video Processing and Recognition: OpenCV, MediaPipe (FaceMesh)
# - Process the photo frames so that the pixels make sense to get parsed together
# - Let the media pipes get through the pipeline, meshing up the images with grids
# - Tune the parameters based on the variances of local positions on faces

# HW0: Read the following code and try to figure out how each line functions
# Task 1: Object Detection

import os
import cv2
import numpy as np

# load the Caffe Net from the object
pwd = "/Users/qaz1214/Downloads/CMA/hs_project/classes/face-detection-with-OpenCV-and-DNN-master" # need to generalize
pretrained_model = cv2.dnn.readNetFromCaffe(os.path.join(pwd,'deploy.prototxt.txt'), os.path.join(pwd,'res10_300x300_ssd_iter_140000.caffemodel')) # *

def obj_detect():
    cap = cv2.VideoCapture(1) # change to 0 or 1 if needed; usually 0 works

    if not cap.isOpened(): # check the camera
        print("Error: Couldn't open the camera.")
    else:
        ret, frame = cap.read()
        if not ret:
            print("Error: Couldn't read a frame from the camera.")
        else:
            # process the current frame
            cv2.imshow("Frame", frame) # *

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        h, w = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0)) # *
        pretrained_model.setInput(blob)
        detections = pretrained_model.forward() # *

        # *
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
        # *

        cv2.imshow('Object Detection', frame)
        if cv2.waitKey(3000) & 0xFF == ord('q'): # *
            break

    cap.release()
    cv2.destroyAllWindows()

# obj_detect()

# HW1: Read the following code and try to figure out how each line functions (Optional)
# Task 2: Optical Flow 

def optical_flow():
    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        print("Error: Couldn't open the camera.")
    else:
        ret, frame = cap.read()
        if not ret:
            print("Error: Couldn't read a frame from the camera.")
        else:
            # 此处可以处理帧，例如显示它或应用某些操作
            cv2.imshow("Frame", frame)

    ret, old_frame = cap.read()

    if not ret:
        print("Failed to grab frame!")

    if old_frame is None:
        print("Image not loaded correctly!")

    old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

    lk_params = dict(winSize=(15, 15),maxLevel=2,criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

    p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7) # *

    mask = np.zeros_like(old_frame) # *

    while True:
        ret, frame = cap.read()
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params) # *

        good_new = p1[st == 1]
        good_old = p0[st == 1]

        # *
        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = int(new.ravel()[0]), int(new.ravel()[1])
            c, d = int(old.ravel()[0]), int(old.ravel()[1])
            mask = cv2.line(mask, (a, b), (c, d), (0, 255, 0), 2)
            frame = cv2.circle(frame, (a, b), 5, (0, 255, 0), -1)
        # *

        img = cv2.add(frame, mask)
        cv2.imshow('Optical Flow', img)
        if cv2.waitKey(3000) & 0xFF == ord('q'):
            break

        old_gray = frame_gray.copy()
        p0 = good_new.reshape(-1, 1, 2)

    cap.release()
    cv2.destroyAllWindows()

# optical_flow()

# HW:
# Task 0: Python Basics. In the module of simulate_data.py, we walked through up to simulate_data.
# - What does zip() do? Why do we use zip() instead of any other functions?
# - Can you think of a way that incorporates simulate_blink_rate to define 'activity'? (We will talk about the CV definition later.)
# - Read the API of simulate_data. What does the default parameters do? Change them to generalize our program.
# - *Make everything Object-Oriented.

# Task 1: Machine Learning. We have walked through the basics of linear regression.
# - Implement a version of linear regression without any machine learning libraries.
# - Build a program that calls the simulation data from Task 0 (mainly simulate_data.py):
#   - The program should be Object-Oriented
#   - The first method in the class you write should return the weights of the linear model, based on the activity and inactivity data
#   - The second method should return the weights of another model, based on the weight of the first model and the data.
#   - Compare the weights of the two models. What do they shed light on? Can we generalize up to n (n being a natural number) iterations?
# - Explore the implementation of logistic regression.
# - Read the Introduction of OpenCV library in Python (or C++) up to Image Resizing with OpenCV: https://learnopencv.com/getting-started-with-opencv/
#   - Leave comments for the parts where you do not understand.
#   - Compare the ideas of the basic 'processing' routines we have covered so far. How can the images be decomposed into meaningful units? 

# Task 2: GUI Design and Control
# - Draw any shape that assimilates an 3D object. e.g. it can be a cone, a cube, a pyramid, etc. Reveal the angle of view as well as you can.

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

# - Explore pynput. Build a simple program that allows the user to:
#   - Click on a button that prompts the basic information; parse the information into a list; display the list.
#   - Change the color of the window. The choice of colors can be either user-input or built-in. If user-input, include another button that behaves similarly as the first one does.
#   - Make a timer that records the time since the user runs the program. Before the user shut the program down, display the total amount of time that the program runs in a pop-up window.



# 11/10-11/11

import random

def simulate_blink_rate(num_intervals):
    """Blink Rate Data:
    - Decide on a time interval for your simulation (e.g., 1 minute).
    - Generate random numbers representing blink counts for each time interval."""
    blink_data = []
    for _ in range(num_intervals):
        blink_count = random.randint(2, 40)  # Adjust the range as needed
        blink_data.append(blink_count)
    return blink_data

def simulate_usage_time(session_duration_minutes, max_interval_duration_minutes):
    """
    Usage Time Data:
    - Define a session duration (e.g., 8 hours for a typical workday).
    - Divide the session into intervals (e.g., 30 minutes each).
    - Ensure that the total usage time doesn't exceed the session duration.
    """
    #Session_duration minutes: How long the dude is gonna use the computer
    #Max interval duration minutes: How long can the dude use pc in 1 interval
    usage_data = []
    remaining_time = session_duration_minutes

    while remaining_time > 0:
        activity_duration = min(random.randint(10, max_interval_duration_minutes), remaining_time)
        usage_data.append(activity_duration)
        remaining_time -= activity_duration + 1 # Add 1 to avoid consecutive inactivity periods

    return usage_data

def simulate_inactivity(usage_data):
    """
    Inactivity Data:
    - Randomly generate inactivity periods within the activity session duration.
    """
    inactivity_data = []
    for duration in usage_data:
        inactivity_duration = random.randint(0, duration // 2)
        #Can't be inactive more than half of session time
        inactivity_data.append(inactivity_duration)
    return inactivity_data

def simulate_activity_labels(inactivity_data, activity_data, threshold_ratio, activity_threshold):
    """
    Activity Labels:
    - Based on your criteria (e.g., if the ratio of inactivity time to activity time exceeds a threshold,
    label it as "break needed"), assign labels to each interval of simulated data.
    """
    activity_labels = []
    # i = 0
    for inactivity_duration, activity_duration in zip(inactivity_data, activity_data):
        # print(inactivity_duration / activity_duration)
        #Inactive is referred as away from the computer, and active is at the computer
        if activity_duration > activity_threshold and (inactivity_duration / activity_duration) <= threshold_ratio:
            activity_labels.append("break needed")
            # print(inactivity_duration / activity_duration)
            # i += 1
        else:
            activity_labels.append("no break needed")
    # print(i)
    return activity_labels

def simulate_data(inactivity_threshold_ratio, activity_threshold):
    # Simulate usage time for 2 months of 8-hour workday with 30-minute intervals
    usage_data = simulate_usage_time(60 * 8 * 60, 60)
    #print(usage_data)

    # Simulate inactivity for a 4-hour session with a 5-minute threshold
    inactivity_data = simulate_inactivity(usage_data)
    #print(inactivity_data)

    # Simulate activity labels based on the ratio of inactivity time to activity time
    activity_labels = simulate_activity_labels(inactivity_data, usage_data, inactivity_threshold_ratio, activity_threshold)
    #print(activity_labels)
    return usage_data, inactivity_data, activity_labels

# HW 11/10:
# Task 0: Python Basics. In the module of simulate_data.py, we walked through up to simulate_data.
# - What does zip() do? Why do we use zip() instead of any other functions?
# For given 2 inputs of two arrays, function returns a array with multiple subarrays that contain the same-index item if you use the tuple function so its visible.
#Otherwise, it will print za zip object

a = ["A", "B", "C"]
b = ["D", "E", "F"]
a.append("X")
b.append("Y")
x = list(zip(a,b))
# print(x)

# - Can you think of a way that incorporates simulate_blink_rate to define 'activity'? (We will talk about the CV definition later.)
# I guess the simulate_blink_rate function can define activity because if the user isn't blinking at all, or is blinking very little, that may mean that he is away from his computer, and if he blinks alot of rubs his eyes then that means he is using his computer.
# print(simulate_blink_rate(1000))

test_data_1 = [11, 10, 7, 18, 28, 15, 12, 2, 7, 3, 16, 3, 22, 17, 21, 15, 18, 12, 24, 24, 3, 15, 11, 29, 19, 9, 1, 17, 11, 18, 25, 24, 15, 22, 12, 12, 3,
               5, 6, 21, 13, 26, 30, 10, 2, 9, 13, 27, 25, 10, 20, 23, 17, 29, 16, 20, 30, 3, 17, 28, 24, 5, 26, 28, 5, 14, 12, 23, 16, 9, 19, 17, 8, 21,
               23, 3, 1, 21, 29, 3, 20, 29, 10, 13, 6, 29, 13, 3, 30, 25, 28, 29, 29, 8, 27, 7, 27, 11, 5, 2, 13, 23, 24, 27, 5, 5, 10, 7, 26, 12, 16, 0,
               27, 7, 5, 18, 6, 9, 14, 16, 0, 11, 0, 21, 16, 4, 17, 19, 4, 13, 19, 10, 6, 5, 11, 22, 20, 16, 14, 0, 16, 23, 22, 17, 20, 11, 10, 21, 25, 6,
               24, 7, 28, 23, 24, 8, 22, 23, 24, 20, 3, 14, 7, 29, 19, 10, 19, 27, 13, 4, 27, 19, 26, 6, 15, 20, 29, 17, 25, 29, 3, 13, 24, 22, 17, 22, 21,
               14, 15, 18, 3, 15, 21, 29, 26, 10, 11, 14, 9, 26, 28, 14, 23, 16, 12, 24, 30, 3, 24, 26, 14, 10, 30, 4, 19, 28, 1, 30, 16, 4, 25, 16, 11, 6,
               2, 5, 22, 30, 13, 23, 4, 5, 23, 22, 2, 29, 8, 10, 16, 30, 10, 7, 22, 17, 27, 29, 5, 24, 26, 1, 2, 13, 30, 23, 0, 17, 9, 17, 9, 23, 20, 21, 2,
               23, 3, 6, 27, 11, 15, 29, 9, 11, 26, 0, 12, 17, 13, 29, 2, 16, 14, 13, 2, 4, 26, 15, 30, 4, 24, 20, 22, 28, 29, 10, 3, 14, 3, 7, 10, 27, 22,
               29, 7, 5, 24, 11, 6, 26, 12, 28, 26, 3, 13, 11, 25, 29, 27, 30, 23, 3, 5, 9, 11, 13, 14, 20, 14, 21, 0, 25, 23, 1, 26, 23, 13, 17, 4, 19, 9,
               26, 28, 7, 12, 26, 0, 13, 8, 11, 30, 24, 14, 27, 15, 14, 11, 4, 26, 8, 20, 21, 4, 27, 20, 21, 18, 5, 27, 6, 6, 18, 24, 7, 8, 8, 11, 4, 18, 9,
               12, 24, 26, 14, 22, 15, 23, 0, 19, 13, 0, 23, 6, 8, 2, 4, 28, 15, 8, 10, 10, 1, 16, 16, 5, 16]
test_data_2 = [18, 5, 28, 12, 29, 33, 6, 4, 29, 35, 23, 34, 16, 13, 6, 38, 27, 21, 38, 36, 23, 3, 2, 35, 8, 12, 31, 23, 19, 17, 4, 20, 18, 32, 8, 11, 15,
               20, 39, 12, 12, 33, 4, 26, 14, 3, 13, 5, 40, 30, 31, 9, 4, 4, 27, 37, 10, 2, 6, 11, 25, 7, 3, 15, 18, 27, 13, 17, 27, 37, 23, 33, 29, 31, 28, 25, 19, 12,
               30, 26, 37, 29, 20, 16, 28, 6, 6, 34, 25, 24, 28, 4, 8, 2, 34, 5, 23, 5, 15, 2, 3, 15, 37, 33, 19, 9, 39, 3, 29, 21, 26, 7, 17, 18, 37, 30, 8, 32, 31, 21,
               30, 3, 22, 25, 29, 10, 16, 5, 30, 13, 10, 19, 29, 35, 31, 11, 37, 18, 30, 30, 19, 5, 25, 3, 19, 26, 4, 16, 24, 39, 19, 7, 10,36, 22, 18, 11, 18, 11, 5,
               37, 9, 35, 6, 32, 22, 27, 13, 2, 6, 36, 33, 31, 28, 26, 26, 37, 6, 13, 33, 26, 28, 24, 14, 6, 17, 17, 16, 9, 35, 11, 37, 34, 34, 29, 23, 2, 22, 19, 4,
               23, 37, 16, 39, 6, 38, 2, 30, 11, 2, 19, 20, 25, 34, 39, 15, 26, 22, 30, 25, 34, 7, 31, 26, 9, 16, 37, 21, 28, 36, 12, 25, 26, 33, 29, 29, 37, 3, 34,
               26, 38, 29, 22, 26, 16, 15, 29, 15, 32, 17, 6, 31, 2, 35, 5, 26, 16, 24, 21, 7, 32, 29, 19, 37, 22, 22, 21, 25, 5, 18, 40, 38, 28, 34, 24, 4, 32, 15,
               6, 31, 17, 22, 29, 5, 8, 18, 22, 19]
test_data_all = [test_data_1, test_data_2]

# HW 11/11:
# Task 0. pynput.mouse: write a program that -
#   - defines a range on the screen where the mouse CAN BE put in
#   - detect the mouse and determine if the mouse is within the range
#   - if the mouse is not within the range, report where it is and print a warning message
#   - otherwise print "LEGIT LOCATION"

# Task 1. compute the standard deviation of both test data, respectively
# - standard deviation:
#   - say you have test_data_1 handy, the difference WITHIN that test data is measured as standard deviation
#   - e.g. 11 and 10, they differ by 1; 28 and 15, they differ by 13; but now I want to understand the amount of difference IN AVERAGE
#   - compute the average for the test data first of all
#   - and then for every instance within the test data, take the absolute difference between this instance and the average, with a square power applied (3^2 = 9)
#   - once we approach every square of the absolute difference, we sum them up, divide them by the count of instances
#   - e.g. we have 20 as our average, and now the data points are [10, 30, 5, 20, 35], (|10 - 20|)^2 = 

# Task 2. Read the API of simulate_data. What does the default parameters do? Change them to generalize our program.
# Threshold ratio is a ratio used to determine if user needs break, and activite threshold is the time set for a break

# - Make everything Object-Oriented. To simplify code, "less is more", i.e. when you see repetition, that means we can simplify
# I don't know how to do this

class blink_rate_statistic: # statistic: measures of blink rate
    def __init__(self, test_data):
        self.blink_rate_data = test_data
        self.average = 0 # instance variable of blink_rate_statistic
        self.standard_deviation = 0

    def get_average_blink_rate(self):
        average_blink_rates = []
        for i in range(len(self.blink_rate_data)):
            total = 0
            test_data_array = self.blink_rate_data[i]
            length = len(test_data_array)
            for w in range(length):
                total += test_data_array[w]
            average_blink_rates.append(total / length) 
        return average_blink_rates

    def get_stand_deviation_blink_rate(self):
        average_blink_rates = self.get_average_blink_rate()
        totals = []
        for w in range(len(self.blink_rate_data)):
            for i in range(len(self.blink_rate_data[w])):
                totals.append(0)
                totals[w] += (abs(average_blink_rates[w] - self.blink_rate_data[w][i])) * (abs(average_blink_rates[w] - self.blink_rate_data[w][i]))
        standard_deviation_1 = totals[0] / (len(self.blink_rate_data[0]))
        standard_deviation_2 = totals[1]/ (len(self.blink_rate_data[1]))
        return standard_deviation_1, standard_deviation_2

my_obj = blink_rate_statistic(test_data_all)
# print(my_obj.get_stand_deviation_blink_rate())
# Output: (77.16073791785124, 122.33637152777777)



# 11/17-11/18

# 11/17:

from pynput.mouse import Listener

def on_move(x, y):
    print('Pointer moved to {0}'.format((x, y)))

def on_click(x, y, button, pressed):
    if pressed:
        print('Mouse clicked at {0}'.format((x, y)))

def on_scroll(x, y, dx, dy):
    print('Mouse scrolled at {0}'.format((x, y)))

# Collect events until released
"""
with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
"""
"""
with open("C:\\Users\\Cyber\\Desktop\\Misc\\Code files\\Learn\\myfile.txt",'w') as file:
    file.write('hello world!\nsup')
"""

# blah = "b"
# print("blah", blah)
# print(f"blah {blah}")
# print("Key pressed:", key_str, ", Count:", key_counts[key_str])
# f is another keyword that allows whatever variable to be plotted into the print statement

from pynput import keyboard

# create the diccionary to store the key count
key_counts = {}

# 
def on_press(key):
    try:
        # 
        key_str = key.char
    except AttributeError: # like a pcall function in Lua, runs top if no error, runs bottom if top errors. 
        # 
        key_str = str(key)
    """
    key_str = key.char
    """
    # try-except keyword

    # 
    if key_str in key_counts: 
        key_counts[key_str] += 1 #If user has already pressed key before
    else:
        key_counts[key_str] = 1

    print(f"Key pressed: {key_str}, Count: {key_counts[key_str]}")

# stops the code from printing more
def on_release(key):
    # ESC kep is pressed, code ends with a return False statement
    if key == keyboard.Key.esc:
        return False

"""
# 
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
"""

# HW 11/17:

# Machine Learning. We have walked through the basics of linear regression.

# - Implement a version of linear regression without any machine learning libraries.
# - Build a program that calls the simulation data from Task 0 (mainly simulate_data.py):
#   - The program should be Object-Oriented
#   - The first method in the class you write should return the weights of the linear model, based on the activity and inactivity data
#   - The second method should return the weights of another model, based on the weight of the first model and the data.
#   - Compare the weights of the two models. What do they shed light on? Can we generalize up to n (n being a natural number) iterations?

# 11/18:

# How can I calculate weight?

def weight_caculation(list):
     n = len(list)
     return n

# print(weight_caculation(simulate_data(0.15,30)[0]))

class checkList:
    def __init__(self):
        self.list1 = simulate_data(0.15,30)[0]
        self.list2 = simulate_data(0.15,30)[0]
    def weight1(self):
        self.total = 0
        self.length = 0
        for value in self.list1:
                self.total += value
                self.length += 1
        #print(self.total / self.length)
    def weight2(self):
        self.total = 0
        self.length = 0
        for value in self.list1:
                self.total += value
                self.length += 1
        for value in self.list2:
                self.total += value
                self.length += 1
        #print(self.total / self.length)

obj = checkList()
# obj.weight1()
# obj.weight2()

# process: the DISTRIBUTED manner of allocating computing resources of hardware
# e.g. 16 gigabytes of RAM
# mouse occupies 500 milibytes of RAM

# The code basically makes (inserts) the object on a system level
# i.e.
# the with keyword inserts the Listener into the system

# l = Listener(..)
# l.join()
# RuntimeError: cannot join thread before it is started
# need to invoke the process from the system, instead of just the running environment

# with open: gets something from the root access of the SYSTEM
# the 'w' argument invokes the writing mode
# 'r', 'w', '', etc. are the levels of access from the SYSTEM

# HW 11/18: debug and simplify the code for the Exercise, even more. there is a major error and a minor refactoring to do.



# 11/24-11/25 (Thanksgiving)
