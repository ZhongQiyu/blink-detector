9.17.2023 - 2.3.2024
# Coding Minds Academy: CS Screen Usage AI Project (eyes_rest)

**This is a mirror of the HS Project in CMA.**

## Homework (2/2/2024):

0. We would tackle them at the same time! Treat the project as one of your HW for the semester. A for Allen, and J for Jimmy.

1. Implementation: (A)
- Allen's hardware support on mediapipe and pynput with the virtual camera.
   - Allen is using PyQt5 and Dlib as alternatives, but it would still be better to figure out mediapipe on macOS and the Windows VM.
   - Refer to the API of CMake and Bazel.
- The fine-tuning module of eye-blink tracing. Methodology: ``
   - Currently we are combining the CascadeClassifier in OpenCV (?) and the Face Mesh (`mediapipe.solutions.face_mesh`) to count the eye blinks.
   - For the captions a bit away from the camera, the model can perform better.
   - Why do you think we are experiencing that? How may we solve this?
   - Refer to the MediaPipe API.
- A better layout a.k.a arrangement of elements for the controlling GUI.
   - Replace the warning messages with pop-up windows to show the moments of stopping the video input.
   - Currently our placement of the display is about 70% on the left, while the GUI on the right can be a bit smaller. Save space for the video display and detection to be 75-80%. Try to truncate the warning messages and the contents of the buttons.

2. Refactoring: (J; *A needs J's approval and synchronization of env vars*)
- In our current working directory (hs_project):
   - Rename the variables and the functions that are too general.
   - Merge System.py, cascade.py, ocr.py, and main.py. Which file can be deleted? Which files should go to which directory? Why?
   - Refer to the repository done by Marisabel. Which files are the ones we inherited? Which are not? Can they be consolidated into one folder?
- Apply the same logic of (1) and (2) on the folders. Do not change them into submodules. Warning: Before ANY kinds of deletion, what would we better do? Hint: Modularity sounds a good plan.

3. Synchronization: (J; Git)
- Make pull requests for your forked repository with mine. I am making my requests based on `pauseForSight` too.
- In the working directory that you have on your computer, upload ALL the dependencies in a folder as requirements.txt.
- Run the command lines to install the Pyinstaller library. Try to wrap up your current version of code with Pyinstaller as an .exe so that it COMPILES and RUNS.

4. Final Compilation! (A and J)
- *The due date is 2/3/2024.*
- Pack the current version as an .exe. (J)
- Make a new demo for the project once you have a running version. (J) Change the code to website of pauseForSight when the new demo is done. (A)

5. *Additional Features:
- A grid layout or a drop-down menu for GUI.
- The location of mouse clicks on the screen.
- The real-time tracking of the most recent keyboard input.
- The statistics of the # of the real-time eye-tracking feature points.
- A script that generalizes the libraries used in both macOS and Windows.
- Run with VS Code or PyCharm to compare and to test the difference of compilation time. Colab prevents the GUI parts to load, and it is the full-size compilers that helps us.
- A fine-tuning threshold of key strokes from both the keyboard and the mouse that tells the user if they needs a break. We have the default parameters set up, while we need additional efforts to let it broadcast to different kinds of tasks.
- A script that connects your external hardware as a virtual camera to work on OpenCV. Since we need to display the project in Zoom, we need to leave the embedded camera for the main project while enabling video input for Zoom with the virtual camera.
- A dynamic procedure that captures and adjusts the detection model's confidence (i.e. the user's confidence too as they calls the GUI) for eye-blinking. The further you are away from the screen, the less difference of the eyelids is needed for telling 1 blink, vice versa.
- Aside from the current text-input box that changes the strictness, enhance the AI feature's controls on the user's end.
   - If the video stream is blocked too much by external items, the dynamic adjustment pauses the streaming, until the blocking items are removed.
   - We will have a time-lapse here, say like a 3-second threshold.

## Pro-tips:
- Merge with whatever Marisabel has shared with you and use my GitHub repo to synchronize the progress. Again, be aware of the naming of everything.
- Do `git pull` then `git push ...` AS ALWAYS. This will eliminate at least 60% of the clashes.
- When deletion of files happened, revert to the last-updated version. Save the directories often when you finish an iteration.
- Use the GitHub feature in either PyCharm or VS Code to synchronize the progress. It is better than plain-text because of the auto-configuration of the .iml files, etc.
- Tackle with Git when you iterate the versions. We are using the ```main``` branch, and if you want to have you own, feel free to create one. Send pull requests per your version update.
- Work on 2 and 3 mostly. Cite the work from ChatGPT with notes when they bring a large help to your project (e.g. put up a module that works completely or fixed a stingy bug).

## Issues:
- Jimmy's difference of the resolution on camera intake from that of Allen's. Vice Versa.

## Curriculum

### Module 1: AI Introduction

1. AI and scikit-learn
* Topics
    * The Introduction to AI
    * AI in Actions with Sklearn
* References
    * Lecture Slides (
      pptx): [Link](https://drive.google.com/file/d/1QaDNCroT7mR968lUs_43RR8QSu08eNkE/view?usp=sharing)
    * Lecture Slides (
      keynote): [Link](https://docs.google.com/presentation/d/1QfNrK_L4GrO6FQyZTCdpSGkWpw2EHN3M/edit?usp=sharing&ouid=104361959057037146246&rtpof=true&sd=true)
    * Lecture sample: https://youtu.be/EjFanvsr-vk
    * Repl code sample: https://replit.com/@sunyu912/ForsakenTanConversions#main.py
* Milestone and Goals
    * Student understands the major AI/Machine Learning concept (i.e., dataset, training, prediction)
    * Student understands the basic Sklearn Iris flower classification example code

2. Computer Vision to Read a Video/Image
- Setup Environment: python(3) and pip(3)
- Introduction to OpenCV: https://learnopencv.com/getting-started-with-opencv/
- Process Image:
    - Run the read, display and write an image example (with an image)
        - https://learnopencv.com/read-display-and-write-an-image-using-opencv/
    - Run the image resizing example (with an image)
        - https://learnopencv.com/image-resizing-with-opencv/
    - Run the putText example
        - https://www.geeksforgeeks.org/python-opencv-cv2-puttext-method/
    - Run rectangle example
        - https://www.geeksforgeeks.org/python-opencv-cv2-rectangle-method/
- Process Video
    - Run the read, display and write an video example (with a video)
        - From File: https://learnopencv.com/reading-and-writing-videos-using-opencv/
        - ...

```python
import cv2 

# Create a video capture object, in this case we are reading the video from a file
vid_capture = cv2.VideoCapture('<file_path.mp4>') # For webcam change <file_path.mp4> to 0. Eg. vid_capture = cv2.VideoCapture(0)

if (vid_capture.isOpened() == False):
  print("Error opening the video file")
# Read fps and frame count
else:
  # Get frame rate information
  # You can replace 5 with CAP_PROP_FPS as well, they are enumerations
  fps = vid_capture.get(5)
  print('Frames per second : ', fps,'FPS')

  # Get frame count
  # You can replace 7 with CAP_PROP_FRAME_COUNT as well, they are enumerations
  frame_count = vid_capture.get(7)
  print('Frame count : ', frame_count)

while(vid_capture.isOpened()):
  # vid_capture.read() methods returns a tuple, first element is a bool 
  # and the second is frame
  ret, frame = vid_capture.read()
  if ret == True:
    cv2.imshow('Frame',frame)
    # 20 is in milliseconds, try to increase the value, say 50 and observe
    key = cv2.waitKey(20)
    if key == ord('q'):
      break
  else:
    break

# Release the video capture object
vid_capture.release()
cv2.destroyAllWindows()
```

### Module 2: Eyes Blink Engine

#### Learn about Medipipe Face Mesh

MediaPipe is an open-source framework developed by Google that offers ready-to-use Machine Learning models for various
tasks, including face detection and facial landmark estimation. In this tutorial, we will focus on using the MediaPipe
Face Mesh model to detect facial landmarks in images and video streams.

#### Prerequisites

mediapipe Python library installed. You can install it using pip:

```commandline
pip install mediapipe
```

#### Getting Started

1. Import the required libraries:
```python
import cv2
import mediapipe as mp
```

2. Initialize the MediaPipe Face Mesh model:
```python
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()
```

3. Initialize the webcam or load an image:
```python
# To use a webcam, you can initialize it like this:
cap = cv2.VideoCapture(0)

# To use an image, you can load it like this:
# image = cv2.imread('your_image.jpg')
```

4. Create a loop to process frames (for live video):
```python
while True:
   ret, frame = cap.read()
   if not ret:
       break

   # Convert the BGR image to RGB
   rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

   # Process the frame with MediaPipe Face Mesh
   results = face_mesh.process(rgb_frame)
```

5. Draw facial landmarks on the frame:
```python
   if results.multi_face_landmarks:
       for face_landmarks in results.multi_face_landmarks:
           for landmark in face_landmarks.landmark:
               x, y, z = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0]), int(landmark.z * frame.shape[1])
               cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)
```

6. Display the processed frame:
```python
   cv2.imshow('Face Mesh', frame)

   if cv2.waitKey(1) & 0xFF == ord('q'):
       break
```

7. Release the video capture and close the OpenCV window when finished:
```python
cap.release()
cv2.destroyAllWindows()
```

- To run the code with a webcam, make sure you have a webcam connected to your computer. Execute the script, and it will
  open a window displaying the webcam feed with facial landmarks drawn.
- To run the code with an image, uncomment the image loading section and provide the path to your image. Execute the
  script, and it will display the image with facial landmarks drawn.

#### Show Left Eyes

Let's inspect the image that show the canonical face model uv visualization
![canonical_face_model_uv_visualization.png](canonical_face_model_uv_visualization.png)

If we zoom in the image we can get the key-points for the left eyes
![img.png](left_eye.png)

To show only the left eye using the MediaPipe Face Mesh model, you can modify the code by selecting and drawing only the
left eye landmarks. Here's how you can do it:

```python
import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Define the indices for the left eye landmarks
            left_eye_landmark_indices = [33, 246, 161, 160, 159, 158, 157, 173, 133, 155, 154, 153, 145, 144, 163, 7]

            for idx in left_eye_landmark_indices:
                landmark = face_landmarks.landmark[idx]
                x, y, z = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0]), int(
                    landmark.z * frame.shape[1])
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

    cv2.imshow('Left Eye', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

In this modified code, we define the left_eye_landmark_indices list to specify the indices of the landmarks
corresponding to the left eye. We then iterate through these indices and draw circles at the corresponding positions on
the frame. This will show only the landmarks of the left eye, effectively isolating it from the rest of the face
landmarks.

#### Show Right Eyes

#### Eyes Blink Detector
- process_image
    - fetch_face_data
    - landmarks_detection
    - update_blink_data
    - calculate the blink ratio
        - euclidean_distance
        - blink_ratio
    - draw_eyes
    - check_blink_rate
    - show_activity_timer
    - calculate_frame_per_sec
    - reset_values
- tester and the test cases for video input

### Module 3: Mouse and Keyboard Tracker

#### Learn about pynput

- Monitoring the mouse
   - A mouse listener is a threading.Thread, and all callbacks will be invoked from the thread.
   - Call pynput.mouse.Listener.stop from anywhere, raise StopException or return False from a callback to stop the listener.
   - When using the non-blocking version above, the current thread will continue executing.
      - This might be necessary when integrating with other GUI frameworks that incorporate a main-loop.
      - But when run from a script, this will cause the program to terminate immediately.

```python
from pynput import mouse

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
# listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
# listener.start()
```

- Monitoring the keyboard
   - A keyboard listener is a threading.Thread, and all callbacks will be invoked from the thread.
      - Call pynput.keyboard.Listener.stop from anywhere, raise StopException or return False from a callback to stop the
   listener.
      - The key parameter passed to callbacks is a pynput.keyboard.Key, for special keys, a pynput.keyboard.KeyCode for normal
   alphanumeric keys, or just None for unknown keys.
   - When using the non-blocking version above, the current thread will continue executing.
      - This might be necessary when integrating with other GUI frameworks that incorporate a main-loop.
      - But when run from a script, this will cause the program to terminate immediately.

```python
from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
```

#### Keyboard and Mouse Tracker
- Define a callback function for mouse events
- Define a callback function for keyword events
- Track user activity
- Run Tracker
- Test Tracker

### Module 4 - Activity and Inactivity Engine

#### Build Activity and Inactivity Engine
- Simulate Data
    - simulate_blink_rate(num_intervals):
    - simulate_usage_time(session_duration_minutes, max_interval_duration_minutes):
    - simulate_inactivity(usage_data):
    - simulate_activity_labels(inactivity_data, activity_data, threshold_ratio, activity_threshold):
- Run train_model
- Make Predictions

### Module 5 - Build Eyes tracker
- Process Image in a Thread
- Use the AI to predict if a person need to take a break (break_prediction)
- Apply run_engine

### Module 6 - APP desktop
- Follow this curriculum to learn about Tkinter https://quest.codingmind.com/view/713865CE2E1144318BD128843A
- Build the EyeTrackerAPP

## References:
- https://pynput.readthedocs.io/
- https://docs.opencv.org/3.4/d6/d00/tutorial_py_root.html
- https://github.com/google/mediapipe/wiki/MediaPipe-Face-Mesh
- https://developers.google.com/mediapipe/solutions/vision/face_landmarker
- ...
