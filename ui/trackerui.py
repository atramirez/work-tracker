"""
Author: atramirez

Main UI window related items
"""

# Python imports
import tkinter as tk
from enum import IntEnum

# UI imports
from ui.tracker_entry import TrackerEntry
from ui.tracker_tracking import Tracker

class WorkTracker(tk.Tk):
    """

    """
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Work Tracker")
        self.geometry("450x350")
        self._frame = None
        self.switch_frame(TrackerEntry)

    def switch_frame(self, frame_class):
        if self._frame is not None:
            self._frame.destroy()
        self._frame = frame_class(self)
        self._frame.pack()
