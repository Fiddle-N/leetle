def solve(x, y):
    return sum(int(num) for num in format(x ^ y, "b"))
