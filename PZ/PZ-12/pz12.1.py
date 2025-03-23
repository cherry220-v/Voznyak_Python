def multiply_by_last(seq):
    if not seq:
        return []
    last = seq[-1]
    return list(map(lambda x: x * last, seq[:-1])) + [last]

seq = [2, 3, 4, 5]
print(multiply_by_last(seq))
