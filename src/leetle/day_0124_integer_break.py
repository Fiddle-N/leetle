def solve(n):
    # split into many 3s as possible
    # as f(x) = n/x pieces of size x
    # gives product x^(n/x)
    # which is maximised at x = e ≈ 2.718
    # however if 1 is left over, that is useless
    # so convert one of the 3s to 4 instead

    if n == 2:
        return 1
    if n == 3:
        return 2
    if n == 4:
        return 4
    div, mod = divmod(n, 3)
    if mod == 1:
        return 3 ** (div - 1) * 4
    elif mod == 2:
        return 3**div * 2
    else:
        # mod = 0
        return 3**div
