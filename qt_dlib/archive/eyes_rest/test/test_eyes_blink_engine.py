import cv2

from eyes_blink_engine import EyeBlinkDetector

frame_counter = 0
cap = cv2.VideoCapture(0)
eye_blink_detector = EyeBlinkDetector()

while True:
    frame_counter += 1  # frame counter
    ret, frame = cap.read()  # getting frame from camera

    if not ret:
        break  # no more frames break

    frame = eye_blink_detector.process_image(frame, frame_counter)

    cv2.imshow('frame', frame)

    key = cv2.waitKey(2)
    if key == ord('q') or key == ord('Q'):
        break

cv2.destroyAllWindows()
cap.release()
