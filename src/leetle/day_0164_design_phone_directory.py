import heapq

UNAVAILABLE = -1

def solve(n, operations):
  unused = list(range(n))
  heapq.heapify(unused)
  used = set()
  output = []
  for op in operations:
    match op:
      case ['get']:
        try:
          next_num = heapq.heappop(unused)
        except IndexError:
          output.append(UNAVAILABLE)
        else:
          used.add(next_num)
          output.append(next_num)
      case ['check', number]:
        output.append(
          0 <= number < n
          and number not in used
        )
      case ['release', number]:
        if number in used:
          heapq.heappush(unused, number)
          used.remove(number)
        output.append(None)
  return output
