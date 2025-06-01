def solve(s, numRows):
    if numRows == 1:
        return s

    start = 0
    end = numRows - 1
    step = 1

    parsed = [[] for _ in range(numRows)]

    curr = start
    for char in s:
        parsed[curr].append(char)
        if curr == 0:
            step = 1
        elif curr == end:
            step = -1
        curr += step

    return "".join(["".join(row) for row in parsed])
