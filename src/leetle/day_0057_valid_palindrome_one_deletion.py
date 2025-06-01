def solve(s):
    for idx, letter in enumerate(s):
        new_s = s[:idx] + s[idx + 1 :]
        if new_s == new_s[::-1]:
            return True
    return False
