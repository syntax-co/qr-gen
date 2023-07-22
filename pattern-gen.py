import turtle
import tkinter
import itertools





def get_combinations(arr, n):
    return list(itertools.product(*([arr] * n)))
















t = turtle.Turtle()

# sets turtle position
t.penup()
t.setx(-100)
t.sety(100)
t.pendown()

initPos = [
    [-100,100],
    [0,100],
    [100,100],
    [100,0],
    [100,-100],
    [0,-100],
    [-100,-100],
    [-100,0],
    [-100,100]
]
offsets = [0,10,20]
allOffsets = get_combinations(offsets,8)


for i in range(1):
    cSet = allOffsets[400]

    
    for k in range(len(initPos)):
        pass
















tkinter.mainloop()

