from tkinter import *
import random

NUM_ROWS, NUM_COLS = 20, 20
north = [[1 for nn in range(NUM_COLS)] for n in range(NUM_ROWS)]
south = [[1 for ss in range(NUM_COLS)] for s in range(NUM_ROWS)]
east = [[1 for ee in range(NUM_COLS)] for e in range(NUM_ROWS)]
west = [[1 for ww in range(NUM_COLS)] for w in range(NUM_ROWS)]

canvas = Canvas(width=400, height=400, bg='white')
canvas.grid()


def display(NUM_ROWS, NUM_COLS, north, south, east, west):
    canvas.delete("all")
    for r in range(1, NUM_ROWS - 1):
        for c in range(1, NUM_COLS - 1):
            if east[r][c] == 1:
                canvas.create_line(20 * c, 20 * r, 20 * c, 20 * r + 20)
            if west[r][c] == 1:
                canvas.create_line(20 * c + 20, 20 * r, 20 * c + 20, 20 * r + 20)
            if north[r][c] == 1:
                canvas.create_line(20 * c, 20 * r + 20, 20 * c + 20, 20 * r + 20)
            if south[r][c] == 1:
                canvas.create_line(20 * c, 20 * r, 20 * c + 20, 20 * r)
    canvas.update()
    canvas.mainloop()


def generate_maze():
    waiting = [(1, 1)]
    found = {(1, 1)}

    for n in range(NUM_COLS):
        found.add((0, n))
    for s in range(NUM_COLS):
        found.add((NUM_COLS - 1, s))
    for e in range(NUM_ROWS):
        found.add((e, 0))
    for w in range(NUM_ROWS):
        found.add((w, NUM_ROWS - 1))

    while len(waiting) > 0:
        cur = waiting[-1]
        y, x = cur[0], cur[1]
        nn, sn, en, wn = (y + 1, x), (y - 1, x), (y, x - 1), (y, x + 1)
        n, s, e, w = False, False, False, False
        nf = []

        if nn in found:
            n = True
        else:
            nf.append(nn)
        if sn in found:
            s = True
        else:
            nf.append(sn)
        if en in found:
            e = True
        else:
            nf.append(en)
        if wn in found:
            w = True
        else:
            nf.append(wn)

        if n & s & e & w:
            waiting.pop()
        else:
            choice = nf[random.randint(0, len(nf) - 1)]
            if choice == nn:
                north[y][x] = 0
                south[nn[0]][nn[1]] = 0
                waiting.append(nn)
                found.add(nn)
            if choice == sn:
                south[y][x] = 0
                north[sn[0]][sn[1]] = 0
                waiting.append(sn)
                found.add(sn)
            if choice == en:
                east[y][x] = 0
                west[en[0]][en[1]] = 0
                waiting.append(en)
                found.add(en)
            if choice == wn:
                west[y][x] = 0
                east[wn[0]][wn[1]] = 0
                waiting.append(wn)
                found.add(wn)

    east[1][1] = 0
    west[18][18] = 0


generate_maze()
display(NUM_ROWS, NUM_COLS, north, south, east, west)
