def solve(s):
  parsed_s = [
    char.lower()
    for char in s
    if char.isalnum()
  ]
  return parsed_s == list(reversed(parsed_s))
