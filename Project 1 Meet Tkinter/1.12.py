from tkinter import*

root = Tk()

def showkq():
    print('phone Number:'+str(sdt.get()))
    print('pass:'+str(pw.get()))
    print('Remember me: '+str(rm.get()))

sdt = IntVar()
Label(root, text='Employee Number:').grid(row=0, column=0, sticky='ew')
Entry(root, width=40, textvariable=sdt).grid(row=0, column=1, columnspan=2, sticky='ew', pady=3)
sdt.set('12096786')

pw = StringVar()
Label(root, text='Login Password:').grid(row=1, column=0, sticky='w')
Entry(root, show='*', width =40, textvariable=pw).grid(row=1, column=1, columnspan=2, sticky='ew', pady=3)
pw.set('sjfaklsdfjas;ldlf')

rm = BooleanVar()
Checkbutton(root, text='Remember Me', variable=rm).grid(row=2, column=1)
rm.set(True)
Button(root, text='Login', command=showkq).grid(row=2, column=2, padx=20)
root.mainloop()