// EyeTracker.h

#ifndef EYETRACKER_H
#define EYETRACKER_H

#include <opencv2/opencv.hpp>
#include <utility>
#include <tuple>

class EyeTracker {

private:
    bool isTracking;
    std::pair<float, float> currentPosition;
    int blinkCount;
    // 其他私有成员和方法
    cv::VideoCapture cap;
    cv::CascadeClassifier face_cascade;
    cv::CascadeClassifier eyes_cascade;

public:
    EyeTracker();
    ~EyeTracker();

    void StartTracking();
    void StopTracking();
    std::pair<float, float> GetCurrentPosition();
    int GetBlinkCount();
    void UpdateParameters(); 
};

#endif // EYETRACKER_H
