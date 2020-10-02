from turtle import *

pencolor('blue')

for i in range(3,7):
    for j in range(i):
        forward(100)
        left(360/i)
mainloop()
