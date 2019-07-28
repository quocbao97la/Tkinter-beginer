from tkinter import *

root = Tk()

#Adding Menubar in the widget 
menubar = Menu(root)

newfileicon = PhotoImage(file='icons/newfile.gif')
openicon = PhotoImage(file='icons/openfile.gif')
saveicon = PhotoImage(file='icons/save.gif')
undoicon = PhotoImage(file='icons/undo.gif')
redoicon = PhotoImage(file='icons/redo.gif')
cuticon = PhotoImage(file='icons/cut.gif')
copyicon = PhotoImage(file='icons/copy.gif')
pasteicon = PhotoImage(file='icons/paste.gif')

#File menu have New, Open, Save, Save As, and Exit
filemenu = Menu(menubar, tearoff=0)#File menu
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New', accelerator='Ctrl+N', image=newfileicon, compound=LEFT)
filemenu.add_separator()
filemenu.add_command(label='Open', accelerator='Ctrl+O', compound=LEFT, underline=0, image=openicon)
filemenu.add_separator()
filemenu.add_command(label='Save', accelerator='Ctrl+S', compound=LEFT, underline=0, image=saveicon)
filemenu.add_command(label='Save As...', accelerator='Ctrl+Shift+S', compound=LEFT, underline=0)
filemenu.add_separator()
filemenu.add_command(label='Exit', accelerator='Alt+F4', compound=LEFT, underline=0)

#Edit menu have Undo, Redo, Cut, Copy, Paste, Find All, and Select All

editmenu = Menu(menubar, tearoff=0)#Edit menu
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Undo', accelerator='Ctrl+Z', underline=2, compound=LEFT, image=undoicon)
editmenu.add_command(label='Redo', accelerator='Ctrl+Y', underline=0, compound=LEFT, image=redoicon )
editmenu.add_separator()
editmenu.add_command(label='Cut', accelerator='Ctrl+X', compound=LEFT, underline=0, image=cuticon)
editmenu.add_command(label='Copy', accelerator='Ctrl+C', compound=LEFT, underline=0, image=copyicon)
editmenu.add_command(label='Paste', accelerator='Ctrl+V', compound=LEFT, underline=0, image=pasteicon)
editmenu.add_separator()
editmenu.add_radiobutton(label='Find', underline=2)
editmenu.add_separator()
editmenu.add_command(label='Select All', underline=7, accelerator='Ctrl+A')

#View have Show Line Number, Show Info Bar at Bottom, Highlight Current Line, and Themes 




root.config(menu=menubar)

root.mainloop()
