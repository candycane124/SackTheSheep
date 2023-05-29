import tkinter as tk              
from tkinter import font as tkfont
# loading Python Imaging Library
from menu_PYTHON.levels import LevelSelect
from menu_PYTHON.menu import Menu
from game.STS_b2 import *

# from main.shop import shop

class App(tk.Tk):
    '''
    A class that creates the base for the menu screen, able to switch between frames easier

    Methods
    -------
    showFrame() -> widget
        Returns the widget/frame being raised to the top
    exit()
        Closes/exits the program
    changeOnHover()
        Change the color of the button based on its status (hovering or not)
    minWindow()
        Minimizes the window
    normalWindow()
        Opens the desired minimized window
    '''
    def __init__(self):
        '''
        Constructor used to build this object. 
        Initializes the display window.
        '''
        tk.Tk.__init__(self)
        self.wm_geometry("500x500")

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where the frames are going to be stacked on top
        # This will be necessary for the showFrame function
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        #initializing the different pages to be called as a frame
        for F in (Menu, LevelSelect):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # all of the pages are in the same location
            frame.grid(row=0, column=0, sticky="nsew")

        self.showFrame("Menu")

    def showFrame(self, pageName):
        '''
        Show a frame for the given page name

        Parameters
        ----------
        pageName: string
            The page name of the frame that will be stacked on top
        
        Return
        ------
        frame: widget
            The frame currently being raised to the top
        '''
        frame = self.frames[pageName]
        frame.tkraise()
        return frame

    def exit(self):
        '''
        Closes the program
        '''
        return self.destroy()

    def changeOnHover(self, button, colourHover, colourLeave):
        '''
        Changes the background colour of buttons based on their current status; hovered or not

        Parameters
        ----------
        button: widget
            The button this color change is applying to
        colourHover: string
            The colour to display while the button is being hovered
        colourLeave: string
            The colour to display while the button is not being interacted with
        '''
        button.bind("<Enter>", func=lambda e: button.config(background=colourHover))
        button.bind("<Leave>", func=lambda e: button.config(background=colourLeave))

    def minWindow(self):
        '''
        Minimizes the desired window
        '''
        self.state(newstate='iconic') # minimize the menu

    def normalWindow(self, pageName):
        '''
        Grabs the window wishing to be reopened and opens it

        Parameters
        ----------
        pageName: string
            The name of the page wanting to be raised
        '''
        frame = self.showFrame(pageName)
        # update the status of the buttons
        if pageName == "LevelSelect": 
            frame.updateButtons(self)
        self.state(newstate='normal') # return the menu to original size

if __name__ == "__main__": #will run if the program is runned from main.py
    app = App()
    app.title("Sack The Sheep") #adding a title to the window
    app.resizable(0, 0) #disable maximizing window - keeps the window to be 500x500
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

    app.after(1000, app.update)
    # initialise the window
    app.mainloop()