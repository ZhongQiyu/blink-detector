# main.py
from PyQt5.QtWidgets import QApplication
from gui import EyeTrackingApp
from utils import load_configuration
import sys

def main():
    config = load_configuration('config.json')  # 加载配置文件
    app = QApplication(sys.argv)
    ex = EyeTrackingApp(config)  # 将配置传递给 EyeTrackingApp
    ex.start_capture()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
