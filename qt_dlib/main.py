from PyQt5 import QtWidgets, QtCore
import sys
import eye_tracking  # 确保这个模块包含了EyeTracker类及其方法

class Worker(QtCore.QObject):
    updated = QtCore.pyqtSignal(tuple)  # 创建信号，当位置更新时发送

    def run(self):
        self.tracker = eye_tracking.EyeTracker()
        self.tracker.start_tracking()
        while True:
            position = self.tracker.get_current_position()
            self.updated.emit(position)  # 发送信号
            QtCore.QThread.msleep(10)  # 短暂休眠以减少CPU使用

class EyeTrackerUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.worker_thread = QtCore.QThread()  # 创建线程
        self.worker = Worker()  # 创建工作对象
        self.worker.moveToThread(self.worker_thread)  # 将工作对象移动到线程
        self.worker_thread.started.connect(self.worker.run)  # 线程开始时运行run方法
        self.worker.updated.connect(self.update_position)  # 连接更新位置的信号
        self.worker_thread.start()  # 启动线程

    def init_ui(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Eye Tracker')

        self.position_label = QtWidgets.QLabel('Position: (0, 0)', self)
        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.position_label)
        self.setLayout(layout)

        self.show()

    def update_position(self, position):
        self.position_label.setText(f'Position: {position}')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = EyeTrackerUI()
    sys.exit(app.exec_())
