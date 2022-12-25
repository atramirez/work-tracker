"""
Author: atramirez

Main file for program execution
"""

# Python packages
import tkinter as tk

# UI
from ui.trackerui import WorkTracker

if __name__ == "__main__":
    gui = WorkTracker()
    gui.mainloop()
