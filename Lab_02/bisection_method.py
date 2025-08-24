def f(x):
    return 0.5 * x * x * x - x * x

def bisection(f, xl, xu, max_itr=500, eps=0.05):
    if f(xl) * f(xu) > 0:
        print("Wrong guess!")
        return None

    if f(xl) * f(xu) == 0:
        if f(xl) == 0:
            return xl
        else:
            return xu

    itr = 1
    xr_old = (xl + xu) / 2
    while True:
        if f(xl) * f(xr_old) > 0:
            xl = xr_old
        elif f(xu) * f(xr_old) < 0:
            xu = xr_old
        else:
            return xr_old

        xr_new = (xl + xu) / 2
        ae = abs(xr_new - xr_old)
        xr_old = xr_new

        itr += 1
        if ae <= eps or itr > max_itr:
            break

    return xr_old

xl, xu = 1, 3
xr = bisection(f, xl, xu)

if xr is not None:
    print("Root found at:", xr)
else:
    print("No root found.")
