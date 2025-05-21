def solve(s):
  if s == '':
    return 0
  return len(s.split()[-1])
