from math import fabs

def f(x):
    return 0.5 * x * x * x - x * x

def false_position(f, a, b, max_iter=500, eps=0.05):
    if f(a) * f(b) > 0:
        print("Invalid initial guesses. f(a) and f(b) must have opposite signs.")
        return None

    xr_old = a
    for i in range(1, max_iter + 1):
        xr = (a * f(b) - b * f(a)) / (f(b) - f(a))
        ae = fabs(xr - xr_old)
        xr_old = xr

        if fabs(f(xr)) < 1e-6 or ae <= eps:
            return xr

        if f(a) * f(xr) < 0:
            b = xr
        else:
            a = xr

    print("Maximum iterations reached without convergence.")
    return xr

a, b = 1, 3
xr = false_position(f, a, b)

if xr is not None:
    print(f"Root is at x = {xr:.4f}")
    print(f"f(x) = {f(xr):.4f}")
