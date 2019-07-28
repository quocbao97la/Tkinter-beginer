from tkinter import*

root = Tk()

Label(root, text='Yellow', bg='yellow').grid(row=0, column=0)
Label(root, text='Blue', bg='blue').grid(row=1, column=1, columnspan=2, sticky='e')
Label(root, text='Green', bg='green').grid(row=0, column=2)
Label(root, text='Orange', bg='orange').grid(row=0, column=3)

root.mainloop()