import tkinter as tk              
from tkinter import font as tkfont
# loading Python Imaging Library
from menu_PYTHON.levels import LevelSelect
from menu_PYTHON.menu import Menu
from game.STS_b2 import *
# from main.shop import shop

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_geometry("500x500")

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Menu, Shop, LevelSelect):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Menu")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def exit(self):
        return self.destroy()

    def changeOnHover(self, button, colourHover, colourLeave):
        button.bind("<Enter>", func=lambda e: button.config(background=colourHover))
        button.bind("<Leave>", func=lambda e: button.config(background=colourLeave))

    def minWindowPlay(self, level):
        self.state(newstate='iconic') # minimize the menu
        status = startLevel(level) # start the level; store in variable
        return status

    def normalWindow(self):
        self.state(newstate='normal')


class Shop(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the store page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Back", cursor="sb_left_arrow",
                            command=lambda: controller.show_frame("Menu"))

        button1.pack()
        controller.changeOnHover(button1, "green", "white")

if __name__ == "__main__":
    app = SampleApp()
    app.title("Sack The Sheep")
    # define window dimensions width and height
    window_width = 500
    window_height = 500
    # get the screen size of your computer [width and height using the root object as foolows]
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    # Get the window position from the top dynamically as well as position from left or right as follows
    position_top = int(screen_height/2 -window_height/2) -30
    position_right = int(screen_width / 2 - window_width/2)-8
    # to cover the pygame window
    app.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    # initialise the window
    app.mainloop()