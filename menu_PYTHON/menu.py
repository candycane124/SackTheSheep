# import everything from tkinter module
from tkinter import *   
# loading Python Imaging Library
from PIL import ImageTk, Image

# create a tkinter window
root = Tk()             
 
# Open window having dimension 100x100
root.geometry('500x500')
# img = ImageTk.PhotoImage(Image.open("menu_PYTHON/menuAssets/grass-588.jpg"))
# panel = Label(root, image = img)
# panel.pack(side = "top", fill = "x", expand = "yes")

# Add background image
# Add image file
bg = ImageTk.PhotoImage(file = "menu_PYTHON/menuAssets/grass-588.jpg")
  
# Create Canvas
canvas1 = Canvas( root, width = 500, height = 500)
  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image = bg, anchor = "nw")
  
# Title of game - may change to an image?
canvas1.create_text( 250, 100, text = "SACK THE SHEEP")

# Create a Button for exiting the window/program
btnStart = Button(root, text = 'START', bd = '7') #needs to bring user to the next screen; levels or level 1
btnExit = Button(root, text = 'EXIT', bd = '7', command = root.destroy)
 
# Set the position of button at the top of window.  
btnStart.pack(side = 'top')
btnExit.pack(side = 'top')   
 
root.mainloop()