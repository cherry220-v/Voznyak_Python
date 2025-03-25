# Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE

def has_positive_elements(matrix):
    for row in matrix:
        for elem in row:
            if elem > 0:
                return True
    return False

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(has_positive_elements(matrix))