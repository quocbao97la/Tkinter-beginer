from tkinter import*

root = Tk()
#all our code is entered here

#Adding Menubar in the widget 
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0) #filemenu

root.config(menu=menubar) #this line actually displays menu
root.mainloop()