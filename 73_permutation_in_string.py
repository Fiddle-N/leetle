from itertools import permutations

def solve(s1, s2):
  return (
    any(''.join(x) in s2 for x in permutations(s1))
  )
