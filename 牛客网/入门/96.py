import math

x = math.pi

def v(r):
    return 4*x*r*r

list = [1,2,4,9,10,13]
for r in list:
    V = v(r)
    print("%0.2f"%V)
