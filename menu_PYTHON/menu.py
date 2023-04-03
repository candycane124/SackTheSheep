# menu to the game Sack The Sheep
import tkinter as tk
# loading Python Imaging Library
from PIL import ImageTk, Image

def startGame():
    pass

root = tk.Tk()
root.geometry('500x500')

frameA = tk.Frame(width=500, height = 150, background="white")
frameB = tk.Frame(width=500, height = 350, background="green")

frameA.pack(side="top")
frameB.pack(side='top')

frameA.pack_propagate(False)
frameB.pack_propagate(False)

title = ImageTk.PhotoImage( Image.open("SackTheSheep/assets/title.png"), Image.ANTIALIAS)
labelTitle = tk.Label(frameA, image=title)
labelTitle.place(relx=0.5, rely=0.5, anchor='center')

startImg = tk.PhotoImage(file = "SackTheSheep/assets/title.png")

img = ImageTk.PhotoImage(Image.open("SackTheSheep/assets/grass-588.jpg"), Image.ANTIALIAS)
lbl = tk.Label(frameB, image=img)
lbl.place(relx=0.5, rely=0.5,anchor='center')  # Place label in center of parent.

# Add Image
login_btn = tk.PhotoImage(file = "SackTheSheep/assets/test_red.png")

btnStart = tk.Button(frameB, image=login_btn, borderwidth=0, command = startGame()).pack(side="top", pady=(50,10)) #needs to bring user to the next screen; levels or level 1
btnSetting = tk.Button(frameB, image=login_btn, borderwidth=0).pack(side="top", pady=10)
btnExit = tk.Button(frameB, image=login_btn, borderwidth=0, command = root.destroy).pack(side="top", pady=10)

root.mainloop()