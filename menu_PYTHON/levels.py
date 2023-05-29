# level menu to the game Sack The Sheep
import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image

from game.STS_b2 import *
from game.scores import *

class LevelSelect(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # grabbing the info of the newest level user has unlocked
        # levelToPlay = self.readLevel()

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
        # title = ImageTk.PhotoImage(Image.open('menu_PYTHON/menuAssets/LevelSelectV2.png'))
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
        

        hiScoreButton = tk.PhotoImage(file = 'assets/highscore.png')
        # hiScoreButton = self.resizeImage(hiScoreButton, 60, 28)
        # hiScoreButton = initialHiScoreButton.zoom(3, 3)
        # hiScoreButton = hiScoreButton.subsample(4,4)
        hiScoreButtonTitle = tk.Label(self, image=hiScoreButton)

        hiScoreButtonTitle.image = hiScoreButton #keeping a reference, so the iamge shows up
        # labelTitle.pack()

        hiButton = tk.Button(self, image=hiScoreButton, background="#A8D465", cursor="target",
                           command=lambda: [controller.minWindow(), highScore(controller)]) #change the destination
        
        
        button.place(anchor="s", relx=0.15, rely=0.95)
        hiButton.place(anchor="s", relx=0.85, rely=0.95)

        btn1 = tk.Button(self, text="Level 1", cursor="target", font=helv36, command=lambda: [controller.minWindow(), startLevel(1, controller)]) #bring user to level 1 + minimize current window
        btn1.place(relx=0.25, rely=0.6, anchor="center")
        
        controller.changeOnHover(btn1, "green", "white")
        controller.changeOnHover(button, "green", "#A8D465")
        controller.changeOnHover(hiButton, "green", "#A8D465")

        self.updateButtons(controller)
    
    def resizeImage(self, img, newWidth, newHeight):
        oldWidth = img.width()
        oldHeight = img.height()
        newPhotoImage = tk.PhotoImage(width=newWidth, height=newHeight)
        for x in range(newWidth):
            for y in range(newHeight):
                xOld = int(x*oldWidth/newWidth)
                yOld = int(y*oldHeight/newHeight)
                rgb = '#%02x%02x%02x' % img.get(xOld, yOld)
                newPhotoImage.put(rgb, (x, y))
        return newPhotoImage

    def updateButtons(self, controller):
        levelToPlay = self.readLevel()

        btn2 = tk.Button(self, text="Level 2", font=tkFont.Font(family='Helvetica', size=18, weight='bold'), cursor="target", command=lambda: [controller.minWindow(), startLevel(2, controller)]) #bring user to level 2 + minimize current window; should be locked; font=helv36
        btn3 = tk.Button(self, text="Level 3", font=tkFont.Font(family='Helvetica', size=18, weight='bold'), cursor="target", command=lambda: [controller.minWindow(), startLevel(3, controller)]) #bring user to level 3 + minimize current window; should be locked; font=helv36

        btn2.place(relx=0.5, rely=0.6, anchor="center")
        btn3.place(relx=0.75, rely=0.6, anchor="center")

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