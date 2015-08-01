from Tkinter import *


def color_chooser(r, c):
    if r + c >= 4:
        return "green"
    else:
        return "light green"


root = Tk()
for r in range(4):
    for c in range(4):
        Label(root, text='%s' % 2**(r + c), height=5, width=10,
              bg=color_chooser(r, c), padx=10).grid(row=r, column=c)
root.mainloop()
