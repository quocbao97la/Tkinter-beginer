from tkinter import*

root = Tk()

canvas = Canvas(root, width=650, height=480, bg='white')
canvas.pack()

def mouse_press(event):
    print('type: {}'.format(event.type))
    print('widget: {}'.format(event.widget))
    print('num: {}'.format(event.num))
    print('x: {}'.format(event.x))
    print('y: {}'.format(event.y))
canvas.bind('<ButtonPress>', mouse_press)
root.mainloop()
