import math
a = 0.2
b = 0.9
h = 0.05
x = a
while x <= b:
    y = (3 * math.log(x**3) - 2 * math.log(x**2)) / (math.exp(2 + x) + math.exp(3 + x))
    print(f"x = {x:.2f}, y = {y:6f}")
    x += h
