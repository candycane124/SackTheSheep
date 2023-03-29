# import everything from tkinter module
from tkinter import *   
 
# create a tkinter window
root = Tk()             
 
# Open window having dimension 100x100
root.geometry('500x500')
 
# Create a Button for exiting the window/program
btnStart = Button(root, text = 'START', bd = '7')
btnExit = Button(root, text = 'EXIT', bd = '7', command = root.destroy)
 
# Set the position of button on the top of window.  
btnExit.pack(side = 'top')   
 
root.mainloop()