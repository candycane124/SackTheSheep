import tkinter as tk
from menu_PYTHON.menu import *

class Initiater(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self) #initializing screen
        self.wm_title("Sack The Sheep")
        self.wm_geometry("500x500")
        
        self.frame = None
        self.switchFrame(Menu)

    def switchFrame(self, frame1):
        newFrame = frame1(self)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = newFrame
        self.frame.pack()

    def exit(self):
        self.destroy()

if __name__ == "__main__":
    app = Initiater()
    app.mainloop()