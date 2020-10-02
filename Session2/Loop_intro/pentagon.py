from turtle import *

pencolor('green')

for i in range(3,6):
    for j in range(i):
        forward(100)
        left(360/i)

mainloop()