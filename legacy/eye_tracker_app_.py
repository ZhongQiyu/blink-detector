from PyQt5 import QtWidgets, QtGui, QtCore
import cv2
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener, Key

class EyeTrackingApp(QtWidgets.QMainWindow):
    def __init__(self, config):
        super().__init__()
        self.initUI(config)
        self.frame_counter = 0
        self.frame_skip = 2
        self.capture = cv2.VideoCapture(config['video_source'])
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, config['frame_width'])
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, config['frame_height'])
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(30)

        # 初始化监听器
        self.mouse_listener = MouseListener(on_move=self.on_mouse_move)
        self.mouse_listener.start()
        self.keyboard_listener = KeyboardListener(on_press=self.on_key_press)
        self.keyboard_listener.start()

        # 初始化统计数据
        self.total_keystrokes = 0
        self.current_key = ''
        self.mouse_position = (0, 0)
        self.left_eye_position = (0, 0)  # 假设
        self.right_eye_position = (0, 0)  # 假设

    def initUI(self, config):
        self.central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QtWidgets.QHBoxLayout(self.central_widget)
        self.video_label = QtWidgets.QLabel(self)
        self.video_label.setScaledContents(True)
        self.layout.addWidget(self.video_label, 4)

        self.control_panel = QtWidgets.QVBoxLayout()
        self.control_panel.setSpacing(10)  # 减小控制面板中各个元素之间的间距
        self.layout.addLayout(self.control_panel, 1)

        self.key_label = QtWidgets.QLabel("Last Key Pressed: None")
        self.control_panel.addWidget(self.key_label)

        self.key_count_label = QtWidgets.QLabel("Total Keystrokes: 0")
        self.control_panel.addWidget(self.key_count_label)

        self.mouse_label = QtWidgets.QLabel("Mouse Position: (0, 0)")
        self.control_panel.addWidget(self.mouse_label)

        self.left_eye_label = QtWidgets.QLabel("Left Eye Position: (0, 0)")
        self.control_panel.addWidget(self.left_eye_label)

        self.right_eye_label = QtWidgets.QLabel("Right Eye Position: (0, 0)")
        self.control_panel.addWidget(self.right_eye_label)

        self.resize(1920, 1200)
        self.setWindowTitle('Eye Tracking App')
        self.show()

    def on_mouse_move(self, x, y):
        self.mouse_position = (x, y)
        self.mouse_label.setText(f"Mouse Position: {self.mouse_position}")

    def on_key_press(self, key):
        try:
            self.current_key = key.char
        except AttributeError:
            self.current_key = str(key)
        self.total_keystrokes += 1
        self.key_label.setText(f"Last Key Pressed: {self.current_key}")
        self.key_count_label.setText(f"Total Keystrokes: {self.total_keystrokes}")

    def update(self):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.flip(frame, 1)
            frame = cv2.resize(frame, (640, 480))

            # 假设您有方法来检测瞳孔位置
            # self.left_eye_position, self.right_eye_position = self.detect_pupil_positions(frame)
            self.left_eye_label.setText(f"Left Eye Position: {self.left_eye_position}")
            self.right_eye_label.setText(f"Right Eye Position: {self.right_eye_position}")

            self.frame_counter += 1
            height, width, channel = frame.shape
            image = QtGui.QImage(frame.data, width, height, width * channel, QtGui.QImage.Format_RGB888).rgbSwapped()
            self.video_label.setPixmap(QtGui.QPixmap.fromImage(image))

    # 在这里实现 detect_pupil_positions 方法
    # def detect_pupil_positions(self, frame):
    #     ...

    def closeEvent(self, event):
        self.capture.release()
        self.mouse_listener.stop()
        self.keyboard_listener.stop()

# 配置示例
config = {
    'video_source': 0,
    'frame_width': 640,
    'frame_height': 480
}

app = QtWidgets.QApplication([])
window = EyeTrackingApp(config)
app.exec_()
