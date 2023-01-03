import tkinter as tk
from tkinter import ttk

class View(tk.Tk):
    def __init__(self, controller):
        super().__init__() # Calling the constructor method of the parent class - self=tk.Tk()
        self.controller = controller # Connecting controller to view
    
    def main(self):
        self.mainloop() # Creation of window screen