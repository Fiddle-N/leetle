def solve(n):
    return sum([digit == "1" for digit in format(n, "b")])
