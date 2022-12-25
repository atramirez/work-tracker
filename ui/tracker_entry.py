"""
Author: atramirez

This contains items for starting a new job
"""
import tkinter as tk

class TrackerEntry(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(text="Task:").pack()
        tk.Text(self, height=1, width=20).pack()
        tk.Button(self, text="Start", command=self.begin_task).pack()

    def begin_task():
        pass