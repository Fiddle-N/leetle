def solve(num):
  if num == 0:
    return True
  if num < 0:
    return False
    
  num_array = []
  curr = num
  while True:
    dm = divmod(curr, 10)
    if dm == (0, 0):
      break
    # loading the digits in reverse is fine 
    # as we are checking palindromes
    num_array.append(dm[1])
    curr = dm[0]
  return num_array == list(reversed(num_array))
