def solve(n):
    return len([digit for digit in f"{n:b}" if digit == "1"])
