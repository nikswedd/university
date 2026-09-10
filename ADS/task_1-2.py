import math

def f(x):
    return math.exp(x - 1) - x**3 - x

def fa(a, b, eps):
    if f(a) * f(b) > 0:
        return None
    while (b - a) / 2 > eps:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

def fb(a, b, eps):
    if f(a) * f(b) > 0:
        return None
    while abs(b - a) > eps:
        x = a - f(a) * (a - b) / (f(a) - f(b))
        if f(x) == 0:
            return x
        elif f(x) * f(a) < 0:
            b = x
        else:
            a = x
    return x

print(fa(0, 1, 0.00001))
print(fb(0, 1, 0.00001))
