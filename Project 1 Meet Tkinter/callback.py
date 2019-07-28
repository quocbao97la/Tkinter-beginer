from tkinter import*

root = Tk()

def callback(number):
    print(number)

Button(root, text='Button 1', command = lambda: callback(1)).pack()
Button(root, text='Button 2', command = lambda: callback(2)).pack()
Button(root, text='Button 3', command = lambda: callback(3)).pack()

root.mainloop()