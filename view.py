import tkinter as tk
from tkinter import ttk

class View(tk.Tk):

    # Class variables
    PAD = 10
    MAX_BUTTONS_PER_ROW = 4
    BUTTONS_LIST = [
        "%", "CE", "C", "/",
        "7", "8", "9", "X",
        "4", "5", "6", "-",
        "1", "2", "3", "+",
        ".", "0", "Back", "=" 
    ]

    def __init__(self, controller):
        super().__init__() # Calling the constructor method of the parent class - self=tk.Tk()
        self.title("Calculator") # Setting a name for the application

        self.controller = controller # Connecting controller to view
        self.value_var = tk.StringVar() # Creating a value holder which can be used to obtain a string variable inputted by the user

        self._make_main_frame() # Creation of main frame
        self._make_entry() # Creation of entry widget onto main frame
        self._make_buttons()
    
    def main(self):
        """Creation of the window screen"""
        self.mainloop() # Creation of window screen

    def _make_main_frame(self): # Pre-fixed with an _ to show it will only be used as a function within the view class
        """Creation and packing of the main frame which contains the main widgets onto the window screen"""
        self.main_frame = ttk.Frame(self) # Creation of a frame object - Pre-fixed with self to make it an attribute of the view class when called, allowing it to be used by other methods within the view class
        self.main_frame.pack(padx=self.PAD, pady=self.PAD) # Packing frame object and adding padding around the frame
    
    def _make_entry(self): # Pre-fixed with an _ to show it will only be used as a function within the view class
        """Creation and packing of an entry into the main frame"""
        entry = ttk.Entry(self.main_frame, justify="right", textvariable=self.value_var) # Creation of an entry widget to be shown on the main frame, starting the user's cursor from the right, and with a textvariable of value_var
        entry.pack(ipady=self.PAD, fill="x") # Packing entry widget
    
    def _make_buttons(self):
        """Creation of calculator buttons"""
        count = 4
        for button in self.BUTTONS_LIST:
            if count == self.MAX_BUTTONS_PER_ROW:
                frame = ttk.Frame(self.main_frame)
                frame.pack()
                count = 0

            btn = ttk.Button(frame, text=button)
            btn.pack(ipady=self.PAD, side="left")
            count += 1

        # For every 4 buttons packed, we want to create a new frame