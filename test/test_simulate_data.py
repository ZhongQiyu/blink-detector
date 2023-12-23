import pytest

from activity_simulator import ActivitySimulator

class TestActivitySimulator:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.simulator = ActivitySimulator()

    def test_simulate_usage_time(self):
        usage_data = self.simulator.simulate_usage_time()
        assert sum(usage_data) <= self.simulator.workday_minutes, "Total usage time exceeds workday duration"

    def test_inactivity_simulation(self):
        usage_data = [20, 30, 40]
        inactivity_data = self.simulator.simulate_inactivity(usage_data)
        for inactivity, usage in zip(inactivity_data, usage_data):
            assert 0 <= inactivity <= usage // 2, "Inactivity duration is out of expected range"

    def test_activity_labels_simulation(self):
        usage_data = [10, 20, 30]
        inactivity_data = [0, 5, 15]
        labels = self.simulator.simulate_activity_labels(inactivity_data, usage_data)
        assert len(labels) == len(usage_data), "Number of labels does not match number of usage periods"

    def test_simulate_activity_labels():
        # 测试simulate_activity_labels函数的行为
        inactivity_data = [0, 10, 5]
        activity_data = [10, 20, 0]
        activity_labels = self.simulator.simulate_activity_labels(inactivity_data, activity_data, 0.15, 30)
        assert len(activity_labels) == len(activity_data), "Labels length mismatch with activity data length"

    def test_data_simulation(self):
        usage_data, inactivity_data, activity_labels = self.simulator.simulate_data()
        assert len(usage_data) == len(inactivity_data), "Mismatch in lengths of usage and inactivity data"
        assert len(usage_data) == len(activity_labels), "Mismatch in lengths of usage data and activity labels"
