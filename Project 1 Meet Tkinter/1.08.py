from tkinter import*

top = Tk()

Label(top, text='Find:').grid(row=0, column=0, sticky='e')
Entry(top).grid(row=0, column=1, sticky='we', padx=2, pady=2, columnspan=9)
Button(top, text='Find').grid(row=0, column=10, sticky='we', padx=2)

Label(top, text='Replace:').grid(row=1, column=0 ,sticky='w')
Entry(top).grid(row=1, column=1, sticky='we', columnspan=9, padx =2, pady=2)
Button(top, text='Replace').grid(row=1, column=10, sticky='we', padx =2)

Checkbutton(top, text='Match whole word only').grid(row=2, column=1, sticky='w', columnspan=4)
Checkbutton(top, text='Math Case').grid(row=3, column=1, sticky='w', columnspan=4)
Checkbutton(top, text='Wrap around').grid(row=4, column=1, sticky='w', columnspan=4)
Button(top, text='Replace').grid(row=2, column=10, sticky='we', padx=2)


Radiobutton(top, text='Up', value=1).grid(row=3, column=6,sticky='w')
Radiobutton(top, text='Down', value=2).grid(row=3, column=7,columnspan=2, sticky='w')
Button(top, text='Replace All').grid(row=3, column=10, sticky='sw', padx=2)
top.mainloop()