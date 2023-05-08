import tkinter as tk              
from tkinter import font as tkfont
# loading Python Imaging Library
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import font as tkFont
from menu_PYTHON.levels import LevelSelect
from menu_PYTHON.menu import Menu

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
    app.mainloop()