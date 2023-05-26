# level menu to the game Sack The Sheep
import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image

from game.STS_b2 import *

class LevelSelect(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # grabbing the info of the newest level user has unlocked
        levelToPlay = self.readLevel()

        # # run first time at once
        # self.update(controller)

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

        backButton = ImageTk.PhotoImage(Image.open('assets/back.png'))
        backButtonTitle = tk.Label(self, image=backButton)

        backButtonTitle.image = backButton #keeping a reference, so the iamge shows up
        # labelTitle.pack()

        button = tk.Button(self, image=backButton, background="#A8D465", cursor="sb_left_arrow",
                           command=lambda: controller.show_frame("Menu"))
        button.pack(side="bottom", anchor="w", padx=25, pady=15)

        btn1 = tk.Button(self, text="Level 1", cursor="target", font=helv36, command=lambda: [controller.minWindow(), startLevel(1, controller)]) #bring user to level 1 + minimize current window
        btn2 = tk.Button(self, text="Level 2", cursor="target", font=helv36, command=lambda: [controller.minWindow(), startLevel(2, controller)]) #bring user to level 2 + minimize current window; should be locked
        btn3 = tk.Button(self, text="Level 3", cursor="target", font=helv36, command=lambda: [controller.minWindow(), startLevel(3, controller)]) #bring user to level 3 + minimize current window; should be locked

        btn1.place(relx=0.25, rely=0.6, anchor="center")
        btn2.place(relx=0.5, rely=0.6, anchor="center")
        btn3.place(relx=0.75, rely=0.6, anchor="center")

        controller.changeOnHover(btn1, "green", "white")
        controller.changeOnHover(button, "green", "#A8D465")
    

        #checking and changing button states based off of the level user already unlocked
        if levelToPlay == 1.0:
            self.lock(btn2)
            self.lock(btn3)
        
        elif levelToPlay == 2.0:
            self.lock(btn3)
            self.unlock(btn2)

        elif levelToPlay == 3.0:
            self.unlock(btn2)
            self.unlock(btn3)

    def lock(self, btn):
        btn["state"] = "disabled"
        return
    
    def unlock(self, btn):
        btn["state"] = "normal"
        self.controller.changeOnHover(btn, "green", "white")
        return
    
    def readLevel(self):
        with open('game\stats.txt','r') as textFile:
            file_content = textFile.readlines()
            info = list(map(float,file_content[0].split()))
            levelToPlay = info[0]

        return levelToPlay
    
    # def update(self, controller):
    #     self.readLevel()
    #     # run itself again after 1000 ms
    #     controller.after(1000, self.update(controller)) 