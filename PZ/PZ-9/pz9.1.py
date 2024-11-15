def sumHalves(d):
    values = list(d.values())
    half = len(values) // 2
    sumFirstHalf = sum(values[:half])
    sum_secondHalf = sum(values[half:])
    return sumFirstHalf, sum_secondHalf

d = {"a": 10, "b": 20, "c": 30, "d": 40}
firstHalf, secondHalf = sumHalves(d)
print(f"Сумма первой половины: {firstHalf}")
print(f"Сумма второй половины: {secondHalf}")