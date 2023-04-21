# menu to the game Sack The Sheep
import tkinter as tk
from tkinter import ttk
# loading Python Imaging Library
from PIL import ImageTk, Image

class Menu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # frameA = tk.Frame(self)
        # frameB = tk.Frame(self, background="green")
        # frameB.pack(side="top")

        # frameA.__init__(self, parent)
        # frameA.winfo_screenwidth(500)
        # frameA.winfo_screenheight(150)

        # frameB.__init__(self, parent)
        # frameA.winfo_screenwidth(500)
        # frameA.winfo_screenheight(350)
        
        style = ttk.Style()

        

        img = ImageTk.PhotoImage(Image.open('assets/grass-588.jpg'))
        lbl = tk.Label(parent, image=img)
        
        lbl.image = img #keeping a reference, so the image will appear properly
        # lbl.pack()
        lbl.place(relx=0.5, rely=0.5, anchor="center")  # Place label in center of parent.

        # Add Images to buttons
        start_btn = tk.PhotoImage(file = "menu_PYTHON/menuAssets/potentialStart.png") #220 pi x 60 pi
        start_btn.image = start_btn
        shop_btn = tk.PhotoImage(file = "menu_PYTHON/menuAssets/settingsPot.png")
        shop_btn.image = shop_btn
        exit_btn = tk.PhotoImage(file = "menu_PYTHON/menuAssets/exitPot.png")
        exit_btn.image = exit_btn

        btnStart = ttk.Button(parent, image=start_btn, cursor="target") #needs to bring user to the next screen; levels or level 1 ; command=lambda:parent.switchFrame(LevelSelect)
        btnShop = ttk.Button(parent, image=shop_btn, cursor="target") #settings
        btnExit = ttk.Button(parent, image=exit_btn,  cursor="target", command = exit) #exit

        style.theme_use('alt')
        style.configure('TButton', background='#232323', foreground='white')
        style.map('TButton', background=[('active', '#008000')])

        btnStart.pack(side="top", pady=(190,10))
        btnShop.pack(side="top", pady=10)
        btnExit.pack(side="top", pady=(10, 50))

        title = ImageTk.PhotoImage(Image.open('menu_PYTHON/menuAssets/titlePot.png'))
        labelTitle = tk.Label(parent, image=title)

        labelTitle.image = title #keeping a reference, so the iamge shows up
        # labelTitle.pack()
        labelTitle.place(relx=0.5, anchor="n")