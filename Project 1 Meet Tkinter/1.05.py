from tkinter import *

root = Tk()

fr = Frame(root)

Button(fr, text ='ALL IS WELL').pack(side = TOP,anchor = W, fill = X, expand =NO)
Button(fr, text ='BACK TO BASICS').pack(side = TOP, fill = X)
Button(fr, text = 'CATH ME IF U CAN').pack(fill = X)
Button(fr, text ='LEFT').pack(side=LEFT,fill=X)
Button(fr, text='CENTER').pack(side =LEFT, fill = X)
Button(fr, text = 'RIGHT').pack(side =LEFT)
fr.pack()
root.mainloop()