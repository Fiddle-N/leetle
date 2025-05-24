VOWELS = ['a', 'e', 'i', 'o', 'u']

def solve(text):
  return sum(
    char.lower() in VOWELS
    for char in text
  )
