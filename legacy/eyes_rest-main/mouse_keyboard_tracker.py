import threading
import time
from math import ceil

from pynput import keyboard, mouse


class Tracker:
    def __init__(self):
        # Define a global variable to track the last activity time
        self.last_activity_time = time.time()
        self.start_inactive_time = None
        self.inactive_time = 0
        self.total_inactive_time = 0
        # Define the inactivity threshold (in seconds)
        self.inactivity_threshold = 5
        self.timer_started = False
        self.__is_listening = False
        # print(self.userID)
        # Collect events until released
        self.mouse_listener = mouse.Listener(
            on_move=self.__on_move,
            on_click=self.__on_click,
            on_scroll=self.__on_scroll)
        # Collect events until released
        self.keyboard_listener = keyboard.Listener(
            on_release=self.__on_release)

    def set_listening(self, option):
        self.__is_listening = option

    # Define a callback function for mouse events
    def __on_move(self, x, y):
        # Update the last activity time
        self.last_activity_time = time.time()

        # If the timer is not started, start it
        if not self.timer_started:
            print("Timer started.")
            self.timer_started = True
            if self.inactive_time != 0:
                print(self.total_inactive_time)
                self.total_inactive_time += self.inactive_time

    # Define a callback function for mouse events
    def __on_click(self, x, y, button, pressed):
        # Update the last activity time
        self.last_activity_time = time.time()

        # If the timer is not started, start it
        if not self.timer_started:
            print("Timer started.")
            self.timer_started = True
            if self.inactive_time != 0:
                print(self.inactive_time)
                self.total_inactive_time += self.inactive_time

    # Define a callback function for mouse events
    def __on_scroll(self, x, y, dx, dy):
        # Update the last activity time
        self.last_activity_time = time.time()

        # If the timer is not started, start it
        if not self.timer_started:
            print("Timer started.")
            self.timer_started = True
            if self.inactive_time != 0:
                print(self.inactive_time)
                self.total_inactive_time += self.inactive_time

    # Define a callback function for keyword events
    def __on_release(self, key):
        # Update the last activity time
        self.last_activity_time = time.time()

        # If the timer is not started, start it
        if not self.timer_started:
            print("Timer started.")
            self.timer_started = True
            if self.inactive_time != 0:
                print(self.inactive_time)
                self.total_inactive_time += self.inactive_time

    def track_user_activity(self):

        # Start listening for events
        self.keyboard_listener.start()
        self.mouse_listener.start()
        self.timer_started = True
        try:
            while self.__is_listening:
                # Check for inactivity
                if time.time() - self.last_activity_time >= self.inactivity_threshold:
                    # Inactivity detected, stop the timer if it's running
                    if self.timer_started:
                        print("Timer stopped. User is inactive.")
                        self.timer_started = False
                        self.start_inactive_time = time.time()
                    self.inactive_time = self.inactivity_threshold + ceil(time.time() - self.start_inactive_time)
            else:
                self.keyboard_listener.stop()
                self.mouse_listener.stop()
        except KeyboardInterrupt:
            # Stop the listeners when the script is interrupted
            self.keyboard_listener.stop()
            self.mouse_listener.stop()

    def run_tracker(self):
        # Start monitoring tasks in parallel
        monitor_thread = threading.Thread(target=self.track_user_activity)
        monitor_thread.start()
