# В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в 2 раза.

def modify_matrix(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if i != j:
                matrix[i][j] *= 2
    return matrix

# Пример использования
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

modified_matrix = modify_matrix(matrix)
for row in modified_matrix:
    print(row)