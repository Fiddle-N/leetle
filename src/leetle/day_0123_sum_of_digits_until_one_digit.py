def solve(n):
    # assume n is always a positive integer
    curr = n
    while True:
        curr = sum([int(digit) for digit in str(curr)])
        if curr < 10:
            return curr
