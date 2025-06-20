def solve(operations):
    record = []
    for op in operations:
        if op == "C":
            record.pop()
        elif op == "D":
            record.append(record[-1] * 2)
        elif op == "+":
            record.append(record[-1] + record[-2])
        else:
            # op is numeric
            record.append(int(op))
    return sum(record)
