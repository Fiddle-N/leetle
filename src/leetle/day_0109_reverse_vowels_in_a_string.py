VOWELS = "aeiou"

def solve(s):
  vowels = [
    char
    for char in s
    if char in VOWELS
  ]
  return "".join([
    (
      vowels.pop()
      if char in VOWELS
      else char
    )
    for char in s
  ])
