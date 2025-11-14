# TODO turn into O(n) by using dictionary

def solve(s, k):
    start = 0
    end = 1
    longest_substr = 0
    while True:
        end = start + longest_substr + 1
        if end > len(s):
            return longest_substr
        substr = s[start: end]
        distinct_chars = len(set(substr))
        if distinct_chars <= k:
            longest_substr = len(substr)
            continue
        if start < (end - 1):
            start += 1
