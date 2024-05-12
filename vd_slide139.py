def two_sum(nums, target):
    # Tạo một từ điển để lưu trữ giá trị và chỉ số của các số đã xem xét
    seen = {}
    # Duyệt qua mảng
    for i, num in enumerate(nums):
        # Tính toán số cần tìm để có tổng bằng target
        complement = target - num
        # Kiểm tra xem số cần tìm đã xuất hiện trước đó hay chưa
        if complement in seen:
            # Nếu có, trả về chỉ số của hai số
            return [seen[complement], i]
        # Nếu không, lưu trữ giá trị và chỉ số của số hiện tại vào từ điển
        seen[num] = i
    # Trường hợp không có giải pháp (theo đề bài, giả định rằng mỗi đầu vào sẽ có chính xác một giải pháp)
    return []
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)