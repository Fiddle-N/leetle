from collections import Counter

# p and s are the wrong way around in the examples
def solve(s, p):
  p_count = Counter(s)
  # tests all windows of length s in p
  return tuple([
    x
    for x in range(len(p) - len(s) + 1)
    if Counter(p[x : x + len(s)]) == p_count
  ])