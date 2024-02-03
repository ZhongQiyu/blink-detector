from mouse_keyboard_tracker import Tracker

t = Tracker()
t.set_listening(option=True)
t.run_tracker()

import pytest
from unittest.mock import Mock
from eyes_tracker import EyeTracker

class TestEyeTracker:
    @pytest.fixture
    def eye_tracker(self):
        # 创建 EyeTracker 实例
        tracker = EyeTracker()
        # 模拟 EyeBlinkDetector 和 Tracker
        tracker.eye_blink_detector = Mock()
        tracker.tracker = Mock()
        return tracker

    def test_break_prediction(self, eye_tracker):
        # 设置模拟对象的返回值
        eye_tracker.eye_blink_detector.start_time = time.time() - 3600  # 1小时前
        eye_tracker.tracker.inactive_time = 1800  # 30分钟

        # 模拟 predict 函数
        eye_tracker.predict = Mock(return_value="break needed")

        # 调用 break_prediction 方法
        eye_tracker.break_prediction()

        # 验证预测结果是否正确
        assert eye_tracker.prediction == "break needed"
        eye_tracker.predict.assert_called_once_with([3600, 1800])
