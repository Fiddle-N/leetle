def solve(dividend, divisor):
  assert divisor != 0
  if dividend == 0:
    return 0
    
  dividend_sign = -1 if dividend < 0 else 1
  divisor_sign = -1 if divisor < 0 else 1
  
  res_sign = (
    -1
    if dividend_sign != divisor_sign
    else 1
  )
  
  res = 0
  curr = abs(dividend)
  while True:
    curr -= abs(divisor)
    if curr < 0:
      return (
        -res
        if res_sign == -1
        else res
      )
    res += 1
