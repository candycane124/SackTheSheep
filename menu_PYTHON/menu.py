# menu to the game Sack The Sheep
import tkinter as tk
# loading Python Imaging Library
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry('500x500')
# #%% Frames
frameA = tk.Frame(width=500, height = 150, background="white")
frameB = tk.Frame(width=500, height = 350, background="green")
# Nested Frame. framebb is created within frameB without width or height
# framebb = tk.Frame(frameB, background="green")

# title = ImageTk.PhotoImage( Image.open('menu_PYTHON/menuAssets/title.png'), Image.ANTIALIAS)
# labelTitle = tk.Label(root, image=title)
# labelTitle.place(relx=0.5, rely=0.15, anchor='center')

# img = ImageTk.PhotoImage(Image.open('menu_PYTHON/menuAssets/grass-588.jpg'), Image.ANTIALIAS)
# lbl = tk.Label(root, image = img)
# lbl.img = img  # Keep a reference in case this code put is in a function.
# lbl.place(relx=0.5, rely=0.5, anchor='center')  # Place label in center of parent.

# # Add other tkinter widgets.
# button = tk.Button(root, text="Start")
# button.grid(row=0, column=0)
# button = tk.Button(root, text="Continue")
# button.grid(row=0, column=1, padx=10)

frameA.pack(side="top")
frameB.pack(side='top')
# expand is the key parameter to center the framebb within frameB
# framebb.pack(expand=True)

frameA.pack_propagate(False)
frameB.pack_propagate(False)

title = ImageTk.PhotoImage( Image.open('menu_PYTHON/menuAssets/title.png'), Image.ANTIALIAS)
labelTitle = tk.Label(frameA, image=title)
labelTitle.place(relx=0.5, rely=0.5, anchor='center')

startImg = tk.PhotoImage(file = 'menu_PYTHON/menuAssets/title.png')

img = ImageTk.PhotoImage(Image.open('menu_PYTHON/menuAssets/grass-588.jpg'), Image.ANTIALIAS)
lbl = tk.Label(frameB, image=img)
lbl.place(relx=0.5, rely=0.5,anchor='center')  # Place label in center of parent.

btnStart = tk.Button(frameB, text='PLAY', width = '30', height='3', bd='3').pack(side="top", pady=(50,10)) #needs to bring user to the next screen; levels or level 1
btnSetting = tk.Button(frameB, text = 'SETTINGS', width = '30', height='3',bd='3').pack(side="top", pady=10)
btnExit = tk.Button(frameB, text = 'EXIT', width = '30', height='3',bd='3', command = root.destroy).pack(side="top", pady=10)

root.mainloop()