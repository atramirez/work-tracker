"""
Author: atramirez

This contains items that are active when a job is being worked 
"""
import tkinter as tk

class Tracker(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(text="This task is tracking placeholder").pack()
