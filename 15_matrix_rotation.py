def solve(matrix):
  new_matrix = list(
    reversed(row)
    for row in zip(*matrix)
  )
  for y, row in enumerate(new_matrix):
    for x, num in enumerate(row):
      matrix[y][x] = num
  return matrix
