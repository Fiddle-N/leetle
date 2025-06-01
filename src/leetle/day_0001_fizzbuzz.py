def solve(n):
    result = []
    for num in range(1, n + 1):
      str_out = ""
      if num % 3 == 0:
          str_out += "Fizz"
      if num % 5 == 0:
          str_out += "Buzz"
      result.append(str_out if str_out else num)
    return result
