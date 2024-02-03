import math
import time

import cv2
import mediapipe as mp
import numpy as np

import utils


class EyeBlinkDetector:
    def __init__(self):
        self.CLOSED_EYES_FRAME = 3
        self.FONTS = cv2.FONT_HERSHEY_COMPLEX
        self.BLINK_RATIO = 3.8
        # Left eyes indices
        self.LEFT_EYE = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]
        # right eyes indices
        self.RIGHT_EYE = [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246]
        self.MAX_BLINKS_PER_MINUTE = 25
        self.map_face_mesh = mp.solutions.face_mesh
        self.color = [utils.GRAY, utils.YELLOW]
        self.start_time_blink = None
        self.start_time = None
        self.CEF_counter = 0
        self.total_blinks = 0
        self.text = 'no break needed'
        self.is_listening = False
        self.is_face_detected = False

    def reset_values(self):
        self.start_time_blink = None
        self.CEF_counter = 0
        self.total_blinks = 0
        self.text = 'no break needed'
        self.start_time = None
        self.is_face_detected = False

    def landmarksDetection(self, img, results, draw=False):
        img_height, img_width = img.shape[:2]
        mesh_coord = [(int(point.x * img_width), int(point.y * img_height)) for point in
                      results.multi_face_landmarks[0].landmark]
        if draw:
            [cv2.circle(img, p, 2, (0, 255, 0), -1) for p in mesh_coord]

        return mesh_coord

    def euclidean_distance(self, point, point1):
        x, y = point
        x1, y1 = point1
        distance = math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
        return distance

    def blinkRatio(self, landmarks, right_indices, left_indices):
        rh_right = landmarks[right_indices[0]]
        rh_left = landmarks[right_indices[8]]
        rv_top = landmarks[right_indices[12]]
        rv_bottom = landmarks[right_indices[4]]

        lh_right = landmarks[left_indices[0]]
        lh_left = landmarks[left_indices[8]]

        lv_top = landmarks[left_indices[12]]
        lv_bottom = landmarks[left_indices[4]]

        rhDistance = self.euclidean_distance(rh_right, rh_left)
        rvDistance = self.euclidean_distance(rv_top, rv_bottom)

        lvDistance = self.euclidean_distance(lv_top, lv_bottom)
        lhDistance = self.euclidean_distance(lh_right, lh_left)

        reRatio = rhDistance / rvDistance
        leRatio = lhDistance / lvDistance

        ratio = (reRatio + leRatio) / 2

        return ratio

    def process_image(self, frame, frame_counter):
        face_mesh = self.map_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        frame, frame_height, results = self.fetch_face_data(face_mesh, frame)

        if results.multi_face_landmarks:

            if not self.is_face_detected:
                self.is_face_detected = True
                self.start_time_blink = time.time()
                self.start_time = time.time()

            mesh_coords = self.landmarksDetection(frame, results, False)
            self.update_blink_data(frame, frame_height, mesh_coords)
            self.draw_eyes(frame, mesh_coords)
            self.total_blinks, self.text, self.start_time_blink = self.check_blink_rate(
                self.total_blinks, self.start_time_blink, self.text)
            utils.colorBackgroundText(frame, f'Eyes: {self.text}', self.FONTS, 1.0, (30, 300), 2, self.color[0],
                                      self.color[1], 8,
                                      8)
            frame = self.show_activity_timer(frame, self.start_time)
            frame = self.calculate_frame_per_sec(frame, frame_counter, self.start_time)
        else:
            self.reset_values()

        return frame

    def fetch_face_data(self, face_mesh, frame):
        frame = cv2.resize(frame, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
        frame_height, frame_width = frame.shape[:2]
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        results = face_mesh.process(rgb_frame)
        return frame, frame_height, results

    def update_blink_data(self, frame, frame_height, mesh_coords):
        ratio = self.blinkRatio(mesh_coords, self.RIGHT_EYE, self.LEFT_EYE)
        utils.colorBackgroundText(frame, f'Ratio : {round(ratio, 2)}', self.FONTS, 0.7, (30, 100), 2, utils.PINK,
                                  utils.YELLOW)
        if ratio > self.BLINK_RATIO:
            self.CEF_counter += 1
            utils.colorBackgroundText(frame, f'Blink', self.FONTS, 1.7, (int(frame_height / 2), 100), 2,
                                      utils.YELLOW, pad_x=6, pad_y=6)

        if self.CEF_counter > self.CLOSED_EYES_FRAME:
            # print(self.BLINK_RATIO)
            self.total_blinks += 1
            self.CEF_counter = 0
        utils.colorBackgroundText(frame, f'Total Blinks: {self.total_blinks}', self.FONTS, 0.7, (30, 150), 2)

    def draw_eyes(self, frame, mesh_coords):
        cv2.polylines(frame, [np.array([mesh_coords[p] for p in self.LEFT_EYE], dtype=np.int32)], True, utils.GREEN,
                      1, cv2.LINE_AA)
        cv2.polylines(frame, [np.array([mesh_coords[p] for p in self.RIGHT_EYE], dtype=np.int32)], True, utils.GREEN,
                      1, cv2.LINE_AA)

    def show_activity_timer(self, frame, start_time):
        end_time = time.time() - start_time
        frame = utils.textWithBackground(frame, f'Time on Screen: {int(end_time)} sec', self.FONTS, 1.0, (30, 220),
                                         bgOpacity=0.9, textThickness=2)
        return frame

    def calculate_frame_per_sec(self, frame, frame_counter, start_time):
        end_time = time.time() - start_time
        fps = frame_counter / end_time
        frame = utils.textWithBackground(frame, f'FPS: {round(fps, 1)}', self.FONTS, 1.0, (30, 50), bgOpacity=0.9,
                                         textThickness=2)
        return frame

    def check_blink_rate(self, total_blinks, start_time_blink, text):
        elapsed_time = time.time() - start_time_blink
        if elapsed_time >= 60:
            blink_rate = total_blinks / (elapsed_time / 60)
            print(f"Blinks per minute: {blink_rate}")

            if blink_rate > self.MAX_BLINKS_PER_MINUTE:
                print("Eye fatigue")
                text = 'break needed'

            total_blinks = 0
            start_time_blink = time.time()
        return total_blinks, text, start_time_blink
