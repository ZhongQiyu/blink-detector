# import cv2
# import mediapipe as mp
#
# mp_face_mesh = mp.solutions.face_mesh
# face_mesh = mp_face_mesh.FaceMesh()
# # To use a webcam, you can initialize it like this:
# cap = cv2.VideoCapture(0)
#
# # To use an image, you can load it like this:
# # image = cv2.imread('your_image.jpg')
#
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     # Convert the BGR image to RGB
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#
#     # Process the frame with MediaPipe Face Mesh
#     results = face_mesh.process(rgb_frame)
#
#     if results.multi_face_landmarks:
#         for face_landmarks in results.multi_face_landmarks:
#             for landmark in face_landmarks.landmark:
#                 x, y, z = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0]), int(
#                     landmark.z * frame.shape[1])
#                 cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)
#     cv2.imshow('Face Mesh', frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

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
                x, y, z = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0]), int(landmark.z * frame.shape[1])
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

    cv2.imshow('Left Eye', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()