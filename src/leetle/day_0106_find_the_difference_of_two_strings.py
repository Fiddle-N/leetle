from collections import Counter

def solve(s, t):
  # assume valid solution
  # assume all lower case
  count = Counter(s)
  count.subtract(Counter(t))
  for letter, letter_count in count.items():
      if letter_count != 0:
          return letter
