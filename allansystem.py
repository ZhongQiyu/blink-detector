import turtle
import tkinter as tk
import cv2
import time

#t = turtle.Turtle()

class myGui():

    """
    Constructor
    """ 
    def __init__(self):
        self.root = tk.Tk()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.title("AI Timetracker") # program title
        self.root.resizable(True, True)
        self.root.resizable(True, True)

        self.title_txt = tk.Label(self.root, text = "AI Timer", font = ("Arial", 20)) # program window, at the top
        self.title_txt.pack()

        self.make_drag_bar(screen_width)


        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.strictness_textbox = tk.Text(self.frame, font=("Arial", 20), height = 1, width = 5)
        self.button = tk.Button(self.frame, text="Set Strictness", font=("Arial", 20), command = self.onclick_updateBarText)
        self.strictness_textbox.grid(row=0, column=0)
        self.button.grid(row=0, column=1)

        self.bar_text = tk.Label(self.root, text = "Max blink count (Strictness): 0", font = ("Arial", 20))
        self.bar_text.pack()

        self.total_time_elapsed = tk.Label(self.root, text = "Total Time Elapsed: 0", font = ("Arial", 20))
        self.total_time_elapsed.pack()
        self.total_time_count = 0
        self.change_total_time_count()

        self.total_blink_count = tk.Label(self.root, text = "Total Blink Count: 0", font = ("Arial", 20))
        self.total_blink_count.pack()

        self.average_blink_rate = tk.Label(self.root, text = "Average Blink Rate: 0", font = ("Arial", 20))
        self.average_blink_rate.pack()

        self.alarm = tk.Label(self.root, text = "You need a break!", font = ("Arial", 30))
        #self.alarm.pack()

        self.root.mainloop()

    """
    Drag Bar
    """ 
    def make_drag_bar(self, screen_width):
        canvas_width = screen_width * 0.8  # Adjust the canvas width to be 80% of the screen width
        canvas_height = 100  # Keep the canvas height fixed or adjust as needed
        self.canvas = tk.Canvas(self.root, width=canvas_width, height=canvas_height)
        self.canvas.pack()

        self.bar_start = 50
        self.bar_end = canvas_width - 50  # Dynamically set the end of the bar
        self.bar_top = 50
        self.bar_bottom = 50

        # Create a bar on the canvas
        self.canvas.create_line(self.bar_start, self.bar_top, self.bar_end, self.bar_bottom, width=10)
        # Define circle size
        self.circle_radius = 10
        # Adjust the initial position of the circle to be at the edge of the bar
        circle_x = self.bar_start + self.circle_radius
        # Create a circle on the bar
        self.circle = self.canvas.create_oval(circle_x - self.circle_radius, 40, circle_x + self.circle_radius, 60, fill='blue')
        # Bind mouse events to the circle
        self.canvas.tag_bind(self.circle, "<ButtonPress-1>", self.on_drag_start)
        self.canvas.tag_bind(self.circle, "<B1-Motion>", self.on_drag_motion)

    def on_drag_start(self, event):
        # Record the item and its location
        self.drag_data = {"x": event.x, "y": event.y, "item": self.circle}

    def on_drag_motion(self, event):
        # Compute the new position based on the mouse x-coordinate
        new_x1 = event.x - self.circle_radius
        new_x2 = event.x + self.circle_radius
        # Check if the new position is within the bounds of the bar
        if new_x1 >= self.bar_start - self.circle_radius and new_x2 <= self.bar_end + self.circle_radius:
            # Calculate the amount to move
            current_coords = self.canvas.coords(self.drag_data["item"])
            move_x = event.x - (current_coords[0] + self.circle_radius)
            # Move the object the appropriate amount
            self.canvas.move(self.drag_data["item"], move_x, 0)
            # Update the bar text to reflect the new position
            self.updateBarText()

    def onclick_updateBarText(self):
        try:
            count = int(self.strictness_textbox.get("1.0", tk.END).strip())
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            return

        max_count = 75  # Maximum value for strictnesss
        bar_length = self.bar_end - self.bar_start

        if 0 <= count <= max_count:
            scaled_position = (count / max_count) * bar_length
            circle_x = self.bar_start + scaled_position
            self.canvas.coords(self.circle, circle_x - self.circle_radius, 40, circle_x + self.circle_radius, 60)
            self.updateBarText()
        else:
            print(f"Invalid range! Please enter a value between 0 and {max_count}.")

    def updateBarText(self):
        coords = self.canvas.coords(self.circle)
        current_x = (coords[0] + coords[2]) / 2
        max_count = 1500  # Maximum value for the bar count
        bar_length = self.bar_end - self.bar_start
        self.bar_count = ((current_x - self.bar_start) / bar_length) * max_count
        self.bar_text.config(text=f"Max blink count (Strictness): {round(int(self.bar_count) / 20)}")

    """
    Update Total Time Elapsed Function
    """ 
    def change_total_time_count(self):
        self.total_time_elapsed.config(text=f"Total Time Elapsed: {self.total_time_count}")
        self.total_time_count += 1
        self.root.after(1000, self.change_total_time_count) 

my_obj = myGui()

# GUI:
# scale the window to fit your screen (e.g. mine is 2560*1600); can be 1920*1200
# relocate the statistics as a transparent box in top-left/top-right/bottom-left/bottom-right
# design where the buttons and dragger would be (this will be part of my tasks)