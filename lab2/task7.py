import math

a = float(input())
b = float(input())
c = float(input())

d = (b * b) - (4 * a * c)

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(x1, x2)
elif d == 0:
    x = (b * -1) / (2 * a)
    print(x)





