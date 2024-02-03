// EyeTracker.cpp

#include <opencv2/opencv.hpp>
#include <iostream>
#include <vector>
#include "EyeTracker.h"

class EyeTracker {
private:
    cv::VideoCapture cap;
    cv::CascadeClassifier face_cascade;
    cv::CascadeClassifier eyes_cascade;

public:
    EyeTracker() {
        // 加载级联分类器
        if (!face_cascade.load("/path/to/opencv/data/haarcascades/haarcascade_frontalface_default.xml") ||
            !eyes_cascade.load("/path/to/opencv/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml")) {
            std::cerr << "Error loading cascades\n";
            exit(0);
        }
    }

    void StartTracking() {
        cap.open(0); // 打开默认摄像头
        if (!cap.isOpened()) {
            std::cerr << "Error opening video stream\n";
            exit(0);
        }
    }

    std::tuple<int, int> GetCurrentPosition() {
        cv::Mat frame;
        if (!cap.read(frame)) {
            std::cerr << "Error reading frame from camera\n";
            return std::make_tuple(-1, -1);
        }

        std::vector<cv::Rect> faces;
        face_cascade.detectMultiScale(frame, faces);

        for (const auto& face : faces) {
            std::vector<cv::Rect> eyes;
            eyes_cascade.detectMultiScale(frame(face), eyes);

            for (const auto& eye : eyes) {
                cv::Point center(face.x + eye.x + eye.width / 2, face.y + eye.y + eye.height / 2);
                return std::make_tuple(center.x, center.y); // 返回第一个检测到的眼睛的中心位置
            }
        }
        return std::make_tuple(-1, -1); // 如果没有检测到眼睛
    }
};
