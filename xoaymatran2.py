def rotate_matrix(matrix):
    n = len(matrix)

    for i in range(n // 2):
        temp = matrix[i]
        # top = left
        matrix[i] = matrix[n - i - 1]
        # left = bottom
        matrix[n - i - 1] = temp
    for i in range(n):
        for j in range(i + 1, n):
            # right = top
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix
# Test với ma trận ví dụ
original_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result_matrix = rotate_matrix(original_matrix)
# In ma trận kết quả
for row in result_matrix:
    print(row)