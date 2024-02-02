import cv2

# 创建一个OpenCV窗口
cv2.namedWindow("Eye Tracking")

# 打开摄像头
cap = cv2.VideoCapture(0)  # 0表示默认摄像头

# 创建眼睛级联分类器
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    # 读取视频帧
    ret, frame = cap.read()
    if not ret:
        break

    # 将帧转换为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 检测眼睛
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 在图像上绘制检测到的眼睛
    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 显示图像
    cv2.imshow("Eye Tracking", frame)

    # 检测键盘输入，按 'q' 键退出
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# 释放摄像头并关闭OpenCV窗口
cap.release()
cv2.destroyAllWindows()
