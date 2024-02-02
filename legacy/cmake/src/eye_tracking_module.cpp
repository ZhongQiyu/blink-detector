#include <tuple>
#include <pybind11/pybind11.h>

#include "EyeTracker.h"

namespace py = pybind11;

PYBIND11_MODULE(eye_tracking, m) {
    py::class_<EyeTracker>(m, "EyeTracker")
        .def(py::init<>())
        .def("start_tracking", &EyeTracker::StartTracking)
        .def("stop_tracking", &EyeTracker::StopTracking)
        .def("get_current_position", &EyeTracker::GetCurrentPosition)
        .def("get_blink_count", &EyeTracker::GetBlinkCount)
        .def("update_parameters", &EyeTracker::UpdateParameters);
}
