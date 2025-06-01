def solve(arr):
    seen = set()
    new_arr = []
    for num in arr:
        if num not in seen:
            new_arr.append(num)
            seen.add(num)
    return new_arr
