# Из матрицы сформировать массив из положительных четных элементов, найти их
# сумму и среднее арифметическое.

matrix = [
    [1, -2, 3],
    [-4, 5, 6],
    [7, -8, 9]
]
arr = [num for row in matrix for num in row if num > 0 and num % 2 == 0]
total = sum(arr)
average = total / len(arr) if arr else 0

print("Положительные чётные элементы:", arr)
print("Сумма:", total)
print("Среднее арифметическое:", average)