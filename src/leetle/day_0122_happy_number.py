def solve(n):
    if n <= 0:
        return False

    seen = set()
    curr = n
    while True:
        seen.add(curr)
        next_ = sum([int(digit) ** 2 for digit in str(curr)])
        if next_ == 1:
            return True
        elif next_ in seen:
            return False
        curr = next_
