# gui.py

from PyQt5 import QtWidgets, QtGui, QtCore
from eye_tracker import EyeTracker
import cv2

class EyeTrackingApp(QtWidgets.QMainWindow):
    def __init__(self, config):
        super().__init__()
        self.initUI()
        self.eye_tracker = EyeTracker(config)  # 假设 EyeTracker 接收配置作为参数
        self.frame_counter = 0  # 初始化 frame_counter
        self.frame_skip = 2  # 定义N，例如每2帧处理一次
        # 使用配置参数初始化视频捕获
        self.capture = cv2.VideoCapture(config['video_source'])
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, config['frame_width'])
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, config['frame_height'])
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(30)  # 30ms 间隔更新

    def initUI(self):
        self.video_label = QtWidgets.QLabel(self)
        self.video_label.setScaledContents(True)  # 设置视频帧能够缩放以填满 QLabel
        self.setCentralWidget(self.video_label)
        # 设置窗口大小
        self.resize(1920, 1200)  # 根据视频帧分辨率设置窗口大小
        self.setWindowTitle('Eye Tracking App')
        self.show()

    def update(self):
        try:
            ret, frame = self.capture.read()
            if ret:
                frame = cv2.flip(frame, 1)  # 水平翻转图像
                frame = cv2.resize(frame, (640, 480))  # 调整分辨率

                if self.frame_counter % self.frame_skip == 0:
                    frame, blink_detected = self.eye_tracker.track(frame)
                
                self.frame_counter += 1

                height, width, channel = frame.shape
                image = QtGui.QImage(frame.data, width, height, width * channel, QtGui.QImage.Format_RGB888).rgbSwapped()
                self.video_label.setPixmap(QtGui.QPixmap.fromImage(image))
            else:
                print("Warning: 未能从摄像头读取帧。")
        except Exception as e:
            print("Error occurred:", e)

    def start_capture(self):
        self.capture = cv2.VideoCapture(0)
        if not self.capture.isOpened():
            print("Error: 摄像头未成功打开。")
            return
        print("摄像头已成功打开。")
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(30)  # 设置定时器，例如每30毫秒触发一次update

    def closeEvent(self, event):
        self.capture.release()
