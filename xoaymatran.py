def rotate_matrix(matrix):
    # Lấy chiều dài của ma trận
    n = len(matrix)
    # Tạo ma trận kết quả với tất cả giá trị ban đầu là 0
    rotated_matrix = [[0] * n for _ in range(n)]
    # Xoay ma trận
    for i in range(n):
        for j in range(n):
            rotated_matrix[j][n-i-1] = matrix[i][j]
    return rotated_matrix
# Test 
original_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result_matrix = rotate_matrix(original_matrix)
# In ma trận kết quả
for row in result_matrix:
    print(row)