# level menu to the game Sack The Sheep
import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image

from game.STS_b2 import *

class LevelSelect(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        levelComplete1 = True #status of level 1 completion
        levelComplete2 = True #status of level 2 completion

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

        # levelComplete1 = lambda: controller.minWindowPlay(1)
        # play1 = startLevel(1)

        btn1 = tk.Button(self, text="Level 1", cursor="target", font=helv36, command=lambda: [controller.minWindow(), startLevel(1, controller)]) #bring user to level 1 + minimize current window
        btn2 = tk.Button(self, text="Level 2", cursor="target", font=helv36, command=lambda: [controller.minWindow(), startLevel(2, controller)]) #bring user to level 2 + minimize current window; should be locked
        btn3 = tk.Button(self, text="Level 3", cursor="target", font=helv36, command=lambda: [controller.minWindow(), startLevel(3, controller)]) #bring user to level 3 + minimize current window; should be locked

        btn1.place(relx=0.25, rely=0.6, anchor="center")
        btn2.place(relx=0.5, rely=0.6, anchor="center")
        btn3.place(relx=0.75, rely=0.6, anchor="center")

        controller.changeOnHover(btn1, "green", "white")
        controller.changeOnHover(button, "green", "white")

        if levelComplete1 != True and levelComplete2 != True:
            self.lock(btn2)
            self.lock(btn3)
        
        if levelComplete1 == True:
            self.lock(btn3)
            self.unlock(btn2)

        if levelComplete2 == True:
            self.unlock(btn3)
    
    def lock(self, btn):
        btn["state"] = "disabled"
        return
    
    def unlock(self, btn):
        btn["state"] = "normal"
        self.controller.changeOnHover(btn, "green", "white")
        return