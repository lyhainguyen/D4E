from turtle import *
speed(-1)
color('blue')
side_length = 200
for i in range(1,80):
    for j in range(1,5):
        forward(side_length)
        left(90)
    right(10)
    side_length = 0.97*side_length

mainloop()