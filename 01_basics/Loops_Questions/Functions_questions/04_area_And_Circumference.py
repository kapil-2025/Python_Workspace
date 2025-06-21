import math
def circle_stats(radius):
    c=math.pi*radius**2
    a=math.pi*2*radius
    return a,c

print(circle_stats(5))