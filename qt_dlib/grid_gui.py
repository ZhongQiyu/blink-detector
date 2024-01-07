# 导入所需的库
import tkinter as tk
from tkinter import ttk
import threading

# ... [其余导入保持不变]

class EyeTrackingApp:
    def __init__(self, window_title):
        self.root = tk.Tk()
        self.root.state('zoomed')
        self.root.title(window_title)
        self.root.configure(bg='white')

        # 主界面布局使用grid
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # 创建顶部框架
        top_frame = ttk.Frame(self.root, padding=5)
        top_frame.grid(row=0, column=0, sticky='ew')
        top_frame.grid_columnconfigure(1, weight=1)

        # 创建左侧和右侧框架
        left_frame = ttk.Frame(top_frame, padding=5)
        left_frame.grid(row=0, column=0, sticky='ns')
        right_frame = ttk.Frame(top_frame, padding=5)
        right_frame.grid(row=0, column=2, sticky='ns')

        # 创建中间框架（包括显示/隐藏统计数据按钮和视频画布）
        center_frame = ttk.Frame(top_frame, padding=5)
        center_frame.grid(row=0, column=1, sticky='nsew')
        center_frame.grid_rowconfigure(1, weight=1)

        # 显示/隐藏统计数据按钮
        self.toggle_stats_button = ttk.Button(center_frame, text="Show/Hide Statistics", command=self.toggle_statistics)
        self.toggle_stats_button.grid(row=0, column=0, pady=10, padx=10)

        # 视频画布
        self.canvas_video = tk.Canvas(center_frame, bg='white')
        self.canvas_video.grid(row=1, column=0, sticky='nsew', pady=10, padx=10)

        # 在左侧框架中添加其他控件
        # 创建时间统计标签
        self.total_time_label = ttk.Label(left_frame, text="Total Time Elapsed: 0", font=("Arial", 20))
        self.total_time_label.grid(row=0, column=0, sticky='w', padx=10, pady=10)

        # 在右侧框架中添加其他控件
        # 创建点击次数统计标签
        self.total_clicks_label = ttk.Label(right_frame, text="Total Clicks: 0", font=("Arial", 20))
        self.total_clicks_label.grid(row=0, column=0, sticky='w', padx=10, pady=10)

        # 初始化其他属性和线程
        # ...

        self.root.mainloop()

    def toggle_statistics(self):
        # 切换统计信息的显示和隐藏
        if left_frame.winfo_ismapped() and right_frame.winfo_ismapped():
            left_frame.grid_remove()
            right_frame.grid_remove()
        else:
            left_frame.grid()
            right_frame.grid()

    # 其他方法的实现
    # ...

# 启动应用程序
app = EyeTrackingApp("MediaPipe Eye Tracking with Tkinter")
