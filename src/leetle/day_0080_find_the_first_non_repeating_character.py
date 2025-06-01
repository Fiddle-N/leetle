def solve(s):
    last_char = None
    last_count = 0
    for char in s:
        if last_char != char:
            if last_count == 1:
                return last_char
            last_char = char
            last_count = 1
        else:
            # char is repeating
            last_count += 1
    if last_count == 1:
        return last_char
    return ""
