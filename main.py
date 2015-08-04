from Tkinter import *
import random


def generate_unique_pair():
    while True:
        x = random.randrange(4)
        y = random.randrange(4)
        if not random_pool[x][y]:
            random_pool[x][y] = True
            return x, y


def update_position():
    for r in range(4):
        for c in range(4):
            if brd[r][c] != 0:
                random_pool[r][c] = True
            else:
                random_pool[r][c] = False


def key_up(event):
    for c in range(4):
        r_new = 0
        for r in range(4):
            if brd[r][c] != 0:
                brd[r_new][c] = brd[r][c]
                if r != r_new:
                    brd[r][c] = 0
                r_new += 1
    for c in range(4):
        for r in range(3):
            if brd[r][c] != 0 and brd[r + 1][c] == brd[r][c]:
                brd[r][c] *= 2
                brd[r + 1][c] = 0
    for c in range(4):
        r_new = 0
        for r in range(4):
            if brd[r][c] != 0:
                brd[r_new][c] = brd[r][c]
                if r != r_new:
                    brd[r][c] = 0
                r_new += 1
    update_position()
    x, y = generate_unique_pair()
    brd[x][y] = random.randrange(2)*2 + 2
    print_board()


def key_down(event):
    for c in range(4):
        r_new = 3
        for r in range(3, -1, -1):
            if brd[r][c] != 0:
                brd[r_new][c] = brd[r][c]
                if r != r_new:
                    brd[r][c] = 0
                r_new -= 1
    for c in range(4):
        for r in range(3, 0, -1):
            if brd[r][c] != 0 and brd[r][c] == brd[r - 1][c]:
                brd[r][c] *= 2
                brd[r - 1][c] = 0
    for c in range(4):
        r_new = 3
        for r in range(3, -1, -1):
            if brd[r][c] != 0:
                brd[r_new][c] = brd[r][c]
                if r != r_new:
                    brd[r][c] = 0
                r_new -= 1
    update_position()
    x, y = generate_unique_pair()
    brd[x][y] = random.randrange(2)*2 + 2
    print_board()


def key_left(event):
    for r in range(4):
        c_new = 0
        for c in range(4):
            if brd[r][c] != 0:
                brd[r][c_new] = brd[r][c]
                if c_new != c:
                    brd[r][c] = 0
                c_new += 1
    for r in range(4):
        for c in range(3):
            if brd[r][c] != 0 and brd[r][c + 1] == brd[r][c]:
                brd[r][c] *= 2
                brd[r][c + 1] = 0
    for r in range(4):
        c_new = 0
        for c in range(4):
            if brd[r][c] != 0:
                brd[r][c_new] = brd[r][c]
                if c_new != c:
                    brd[r][c] = 0
                c_new += 1
    update_position()
    x, y = generate_unique_pair()
    brd[x][y] = random.randrange(2)*2 + 2
    print_board()


def key_right(event):
    for r in range(4):
        c_new = 3
        for c in range(3, -1, -1):
            if brd[r][c] != 0:
                brd[r][c_new] = brd[r][c]
                if c != c_new:
                    brd[r][c] = 0
                c_new -= 1
    for r in range(4):
        for c in range(3, 0, -1):
            if brd[r][c] != 0 and brd[r][c - 1] == brd[r][c]:
                brd[r][c] *= 2
                brd[r][c - 1] = 0
    for r in range(4):
        c_new = 3
        for c in range(3, -1, -1):
            if brd[r][c] != 0:
                brd[r][c_new] = brd[r][c]
                if c != c_new:
                    brd[r][c] = 0
                c_new -= 1
    update_position()
    x, y = generate_unique_pair()
    brd[x][y] = random.randrange(2)*2 + 2
    print_board()


def color(v):
    if v == 0 or v == 2:
        return '#BCEB91'
    elif v == 4 or v == 8:
        return 'light green'
    elif v == 16 or v == 32:
        return '#78AB46'
    elif v == 64 or v == 128:
        return '#488214'
    elif v == 256 or v == 512:
        return '#458B00'
    elif v == 1024 or v == 2048:
        return '#2B5323'


def print_board():
    for r in range(4):
        for c in range(4):
            labelframe = LabelFrame(frame, relief=FLAT)
            labelframe.grid(row=r, column=c)
            if brd[r][c] != 0:
                label = Label(labelframe, text=str(brd[r][c]),  bg=color(brd[r][c]),
                              height=5, width=10)
                label.pack()

            else:
                label = Label(labelframe,  bg=color(brd[r][c]), height=5, width=10)
                label.pack()


root = Tk(className="2048")
brd = [[0]*4 for i in range(4)]
random_pool = [[False]*4 for i in range(4)]
frame = Frame(root)
frame.focus_set()
frame.pack()
x1, y1 = generate_unique_pair()
x2, y2 = generate_unique_pair()

brd[x1][y1] = random.randrange(2)*2 + 2
brd[x2][y2] = random.randrange(2)*2 + 2

print_board()
frame.bind("<Up>", key_up)
frame.bind("<Down>", key_down)
frame.bind("<Right>", key_right)
frame.bind("<Left>", key_left)

root.mainloop()

