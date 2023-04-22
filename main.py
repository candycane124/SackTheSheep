import tkinter as tk              
from tkinter import font as tkfont
# loading Python Imaging Library
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import font as tkFont

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

        levelComplete1 = False #status of level 1 completion
        levelComplete2 = False #status of level 2 completion

        helv36 = tkFont.Font(family='Helvetica', size=18, weight='bold')

        #Background
        img = ImageTk.PhotoImage(Image.open('assets/grass-588.jpg'))
        lbl = tk.Label(self, image=img)
        
        lbl.image = img #keeping a reference, so the image will appear properly
        # lbl.pack()
        lbl.place(relx=0.5, rely=0.5, anchor="center")  # Place label in center of parent.

        #Title image
        title = ImageTk.PhotoImage(Image.open('menu_PYTHON/menuAssets/LevelTemp.png'))
        labelTitle = tk.Label(self, image=title)

        labelTitle.image = title #keeping a reference, so the iamge shows up
        # labelTitle.pack()
        labelTitle.place(bordermode="inside", anchor="n", relx=0.5)

        button = tk.Button(self, text="Back", cursor="sb_left_arrow",
                           command=lambda: controller.show_frame("Menu"))
        button.pack(side="bottom")

        btn1 = tk.Button(self, text="Level 1", cursor="target", font=helv36) #bring user to level 1
        btn2 = tk.Button(self, text="Level 2", cursor="target", font=helv36) #bring user to level 2; should be locked
        btn3 = tk.Button(self, text="Level 3", cursor="target", font=helv36) #bring user to level 3; should be locked

        btn1.place(relx=0.25, rely=0.6, anchor="center")
        btn2.place(relx=0.5, rely=0.6, anchor="center")
        btn3.place(relx=0.75, rely=0.6, anchor="center")

        controller.changeOnHover(btn1, "green", "white")
        controller.changeOnHover(button, "green", "white")

        if levelComplete1 != True:
            self.lock(btn2)
            self.lock(btn3)
        elif levelComplete2 != True:
            self.lock(btn3)
            self.unlock(btn2)
        else:
            self.unlock(btn3)
    
    def lock(self, btn):
        btn["state"] = "disabled"
        return
    
    def unlock(self, btn):
        btn["state"] = "normal"
        self.controller.changeOnHover(btn, "green", "white")

        return


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()