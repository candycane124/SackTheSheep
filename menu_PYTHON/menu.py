# menu to the game Sack The Sheep
import tkinter as tk
from tkinter import ttk
# loading Python Imaging Library
from PIL import ImageTk, Image
# importing level 1
from ..levels import levels_page

root = tk.Tk()
root.geometry('500x500')
style = ttk.Style()

frameA = tk.Frame(width=500, height = 150, background="light blue")
frameB = tk.Frame(width=500, height = 350)

frameA.pack(side="top")
frameB.pack(side='top')

frameA.pack_propagate(False)
frameB.pack_propagate(False)

title = ImageTk.PhotoImage( Image.open('menu_PYTHON/menuAssets/titlePot.png'), Image.ANTIALIAS)
labelTitle = tk.Label(frameA, image=title)
labelTitle.place(relx=0.5, rely=0.5, anchor='center')

img = ImageTk.PhotoImage(Image.open('assets/grass-588.jpg'), Image.ANTIALIAS)
lbl = tk.Label(frameB, image=img)
lbl.place(relx=0.5, rely=0.5,anchor='center')  # Place label in center of parent.

# Add Image
start_btn = tk.PhotoImage(file = "menu_PYTHON/menuAssets/potentialStart.png")
settings_btn = tk.PhotoImage(file = "menu_PYTHON/menuAssets/settingsPot.png")
exit_btn = tk.PhotoImage(file = "menu_PYTHON/menuAssets/exitPot.png")

btnStart = ttk.Button(frameB, image=start_btn, cursor="target") #needs to bring user to the next screen; levels or level 1
btnSetting = ttk.Button(frameB, image=settings_btn, cursor="target") #settings
btnExit = ttk.Button(frameB, image=exit_btn,  cursor="target", command = root.destroy) #exit

style.theme_use('alt')
style.configure('TButton', background='#232323', foreground='white')
style.map('TButton', background=[('active', '#008000')])
btnStart.pack(side="top", pady=(50,10))
btnSetting.pack(side="top", pady=10)
btnExit.pack(side="top", pady=10)

root.mainloop()