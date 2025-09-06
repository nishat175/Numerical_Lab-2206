def f(x):
    return x**3 - x - 2

def secant(a, b, tol = 1e-6):
    if f(a) == f(b):
        print("Invalid interval!")
        return None

    while abs(b - a) > tol:
        c = b - (f(b) * (b - a)) / (f(b) - f(a))
        if f(c) == 0:
            return c
        a, b = b, c

    return b

root = secant(1, 2)
print("Approximate Root:", root)
