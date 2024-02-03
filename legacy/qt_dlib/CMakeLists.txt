# 设定项目依赖版本
cmake_minimum_required(VERSION 3.4)
project(eye_tracking_module)

# 设置C++标准
set(CMAKE_CXX_STANDARD 11)

# 找到pybind11
find_package(pybind11 REQUIRED)

# 找到OpenCV
find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

# 创建模块
pybind11_add_module(eye_tracking src/eye_tracking_module.cpp)

# 链接pybind11库
add_library(eye_tracking MODULE eye_tracking_module.cpp EyeTracker.cpp)
target_link_libraries(eye_tracking PRIVATE pybind11::module)

# 链接OpenCV库
target_link_libraries(eye_tracking PRIVATE ${OpenCV_LIBS})

# 链接你的眼动追踪库（如果有的话）
# target_link_libraries(eye_tracking PRIVATE your_eye_tracking_library)

# 设定Python版本
set_target_properties(eye_tracking PROPERTIES PREFIX "${PYTHON_MODULE_PREFIX}" SUFFIX "${PYTHON_MODULE_EXTENSION}")