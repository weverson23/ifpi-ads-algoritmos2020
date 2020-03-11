import turtle
import math

def fatia(t,length):
    for i in range(3):
        t.fd(length)
        t.lt(120.0)


def torta(t,n,length):
    for i in range(n):
        fatia(t,length)
        t.lt(360.0/n)



bob = turtle.Turtle()
torta(bob,8,100)
turtle.mainloop()
