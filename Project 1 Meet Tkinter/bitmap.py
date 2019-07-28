from tkinter import *

root = Tk()

mybitmaps = [0xaf]

for i in mybitmaps:
  Button(root, bitmap=i,  width=20, height=20).grid(row=(mybitmaps.index(i)+1), column=4, sticky='nw')


root.mainloop()