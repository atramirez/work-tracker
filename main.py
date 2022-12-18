"""
Author: atramirez

Main file for program execution
"""

# Python packages
import tkinter

# UI
import ui.trackerui as ui

if __name__ == "__main__":
    root = tkinter.Tk()
    gui = ui.WorkTracker(root)
    root.mainloop()
