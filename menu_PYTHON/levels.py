# level menu to the game Sack The Sheep
import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image

from game.STS_b2 import *
from game.scores import *

class LevelSelect(tk.Frame):
    '''
    A class that holds all the components for the level select screen.
    '''
    def __init__(self, parent, controller):
        '''
        Constructor used to build the frame of level select. Initializes the level select screen/frame.
        
        Attributes
        ----------
        parent: widget
            The essential starting frame everything is being built off of.
        controller: widget
            The base all the frames are placed on top of; where all the shared functions are

        Methods
        -------
        updateButtons()
            Updates the status of the buttons
        lock()
            Display the desired button as being locked; cannot be clicked on
        unlock()
            Display the desired button as being unlocked; can be clicked on
        readLevel() -> float
            Returns the player's level completion status as a float
        '''
        tk.Frame.__init__(self, parent)
        self.controller = controller

        helv36 = tkFont.Font(family='Helvetica', size=18, weight='bold')

        #Background
        img = ImageTk.PhotoImage(Image.open('menu_PYTHON/menuAssets/background-grass.png'))
        lbl = tk.Label(self, image=img)
        
        lbl.image = img #keeping a reference, so the image will appear properly
        # lbl.pack()
        lbl.place(relx=0.5, rely=0.5, anchor="center")  # Place label in center of parent.

        #Title image
        title = ImageTk.PhotoImage(Image.open('menu_PYTHON/menuAssets/screen-level.png'))
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
                           command=lambda: controller.showFrame("Menu"))
        

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

    def updateButtons(self, controller):
        '''
        Updates the status of the buttons (level)

        Parameters
        ----------
        controller: widget
            The base all the frames are placed on top of; where all the shared functions are
        
        '''
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
        '''
        Display the button desired as being locked

        Parameters
        ----------
        btn: widget
            The button hoping to appear locked
        '''
        btn["state"] = "disabled"
        return
    
    def unlock(self, btn):
        '''
        Display the button desired as being unlocked

        Parameters
        ----------
        btn: widget
            The button hoping to appear unlocked
        '''
        btn["state"] = "normal"
        self.controller.changeOnHover(btn, "green", "white")
        return
    
    def readLevel(self):
        '''
        Reads the level status of the player

        Return
        ------
        levelToPlay: float
            A number signifying the level the user should have unlocked
        '''
        with open('game\stats.txt','r') as textFile:
            file_content = textFile.readlines()
            info = list(map(float,file_content[0].split()))
            levelToPlay = info[0]

        return levelToPlay