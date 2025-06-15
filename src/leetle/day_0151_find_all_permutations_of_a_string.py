from itertools import permutations

def solve(s):
    return [
      ''.join(perm)
      for perm in permutations(s, len(s))
    ]
 