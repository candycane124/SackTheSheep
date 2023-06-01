# menu to the game Sack The Sheep
import tkinter as tk
from tkinter import ttk
# loading Python Imaging Library
from PIL import ImageTk, Image
from game.shop import shop

class Menu(tk.Frame):
    '''
    A class that contains all the components making up the menu screen.
    '''
    def __init__(self, parent, controller):
        '''
        Constructor used to build the frame. Initializes the menu screen onto the display window.
        
        Attributes
        ----------
        parent: widget
            The essential starting frame everything is being built off of.
        controller: widget
            The base all the frames are placed on top of; where all the shared functions are
        '''
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        #Background
        img = ImageTk.PhotoImage(Image.open('menu_PYTHON/menuAssets/background-grass.png'))
        lbl = tk.Label(self, image=img)
        
        lbl.image = img #keeping a reference, so the image will appear properly
        # lbl.pack()
        lbl.place(relx=0.5, rely=0.5, anchor="center")  # Place label in center of parent.

        #Title image
        title = ImageTk.PhotoImage(Image.open('menu_PYTHON/menuAssets/screen-title.png'))
        labelTitle = tk.Label(self, image=title)

        labelTitle.image = title #keeping a reference, so the iamge shows up
        # labelTitle.pack()
        labelTitle.place(bordermode="inside", anchor="n", relx=0.5)

        # Add Images to buttons
        start_btn = tk.PhotoImage(file = "menu_PYTHON/menuAssets/button-play.png") #220 pi x 60 pi
        shop_btn = tk.PhotoImage(file = "menu_PYTHON/menuAssets/button-shop.png")
        exit_btn = tk.PhotoImage(file = "menu_PYTHON/menuAssets/button-exit.png")

        style = ttk.Style()

        #creating buttons
        btnStart = ttk.Button(self, image=start_btn, cursor="target", command=lambda: controller.showFrame("LevelSelect")) #needs to bring user to the next screen; levels or level 1 ; command=lambda:parent.switchFrame(LevelSelect)
        btnShop = ttk.Button(self, image=shop_btn, cursor="target", command=lambda: [controller.minWindow(), shop(controller)]) #lambda: exec(open('game/shop.py').read())
        btnExit = ttk.Button(self, image=exit_btn,  cursor="target", command = exit) #exit

        #keeping a reference
        btnStart.image = start_btn 
        btnShop.image = shop_btn
        btnExit.image = exit_btn

        #estabilishing style of buttons
        style.theme_use('alt')
        style.configure('TButton', background='#232323', foreground='white')
        style.map('TButton', background=[('active', '#008000')])

        #putting buttons onto the frame
        btnStart.place(relx=0.5, rely=0.5, anchor="center")
        btnShop.place(relx=0.5, rely=0.65, anchor="center")
        btnExit.place(relx=0.5, rely=0.8, anchor="center")