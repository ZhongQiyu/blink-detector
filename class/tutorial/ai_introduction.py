# Module 1
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


# Module 2
import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

# use a webcam
cap = cv2.VideoCapture(0)

# use an image
# image = cv2.imread('your_image.jpg')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Face Mesh
    results = face_mesh.process(rgb_frame)

if results.multi_face_landmarks:
    for face_landmarks in results.multi_face_landmarks:
        for landmark in face_landmarks.landmark:
            x, y, z = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0]), int(landmark.z * frame.shape[1])
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

cv2.imshow('Face Mesh', frame)

"""
if results.multi_face_landmarks:
    for face_landmarks in results.multi_face_landmarks:
        left_eye_landmark_indices = [33, 246, 161, 160, 159, 158, 157, 173, 133, 155, 154, 153, 145, 144, 163, 7] # Define the indices for the left eye landmarks
        for idx in left_eye_landmark_indices: # Extract the locations of the left eyes
            landmark = face_landmarks.landmark[idx]
            x, y, z = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0]), int(landmark.z * frame.shape[1])
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

cv2.imshow('Left Eye', frame)
"""

if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()

# May we align for the identations that are put within the file?
