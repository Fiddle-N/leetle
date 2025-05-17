from collections import defaultdict

def solve(strs):
  grouped = defaultdict(list)
  for str_ in strs:
    grouped[tuple(sorted(str_))].append(str_)
  return list(grouped.values())
