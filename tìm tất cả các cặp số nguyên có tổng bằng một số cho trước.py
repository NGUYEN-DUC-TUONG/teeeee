def find_pairs_with_sum(arr, target_sum):
    pairs = set()  # Sử dụng set để tránh lặp các cặp giống nhau
    # Duyệt qua mảng để tìm cặp số
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                # Nếu tìm thấy cặp, thêm vào set
                pairs.add((arr[i], arr[j]))
    # Chuyển set thành danh sách để in kết quả
    result = list(pairs)
    return result
input_array = [2, 6, 3, 9, 11]
target_sum = 9
result_pairs = find_pairs_with_sum(input_array, target_sum)
print(result_pairs)