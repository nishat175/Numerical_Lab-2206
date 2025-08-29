def f(x):
    return x * (2.71828**x) - 1 

def df(x):
    return (2.71828**x) * (x + 1)

def newton_raphson(x0, tol=1e-6, max_iter=100):
    print("Iteration\t x")
    for i in range(max_iter):
        x1 = x0 - f(x0)/df(x0)
        print(f"{i+1}\t\t {x1:.6f}")
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return None

root = newton_raphson(0.5)
print("\nApproximate Root:", root)
