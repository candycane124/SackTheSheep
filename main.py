import tkinter as tk              
from tkinter import font as tkfont
# loading Python Imaging Library
from PIL import ImageTk, Image
from tkinter import ttk

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


class Shop(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the store page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("Menu"))

        button1.pack()


class Menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        #Background
        img = ImageTk.PhotoImage(Image.open('assets/grass-588.jpg'))
        lbl = tk.Label(self, image=img)
        
        lbl.image = img #keeping a reference, so the image will appear properly
        # lbl.pack()
        lbl.place(relx=0.5, rely=0.5, anchor="center")  # Place label in center of parent.

        #Title image
        title = ImageTk.PhotoImage(Image.open('menu_PYTHON/menuAssets/titlePot.png'))
        labelTitle = tk.Label(self, image=title)

        labelTitle.image = title #keeping a reference, so the iamge shows up
        # labelTitle.pack()
        labelTitle.place(bordermode="inside", anchor="n", relx=0.5)

        # Add Images to buttons
        start_btn = tk.PhotoImage(file = "menu_PYTHON/menuAssets/potentialStart.png") #220 pi x 60 pi
        shop_btn = tk.PhotoImage(file = "menu_PYTHON/menuAssets/settingsPot.png")
        exit_btn = tk.PhotoImage(file = "menu_PYTHON/menuAssets/exitPot.png")

        style = ttk.Style()

        btnStart = ttk.Button(self, image=start_btn, cursor="target", command=lambda: controller.show_frame("LevelSelect")) #needs to bring user to the next screen; levels or level 1 ; command=lambda:parent.switchFrame(LevelSelect)
        btnShop = ttk.Button(self, image=shop_btn, cursor="target", command=lambda: controller.show_frame("Shop")) #shop
        btnExit = ttk.Button(self, image=exit_btn,  cursor="target", command = exit) #exit

        btnStart.image = start_btn #keeping a reference
        btnShop.image = shop_btn #keeping a reference
        btnExit.image = exit_btn #keeping a reference

        style.theme_use('alt')
        style.configure('TButton', background='#232323', foreground='white')
        style.map('TButton', background=[('active', '#008000')])

        btnStart.place(relx=0.5, rely=0.5, anchor="center")
        btnShop.place(relx=0.5, rely=0.65, anchor="center")
        btnExit.place(relx=0.5, rely=0.8, anchor="center")
        


class LevelSelect(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #Title image
        title = ImageTk.PhotoImage(Image.open('menu_PYTHON/menuAssets/LevelTemp.png'))
        labelTitle = tk.Label(self, image=title)

        labelTitle.image = title #keeping a reference, so the iamge shows up
        # labelTitle.pack()
        labelTitle.place(bordermode="inside", anchor="n", relx=0.5)

        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("Menu"))
        button.pack(side="bottom")


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()