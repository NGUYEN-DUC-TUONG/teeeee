import array

# Tạo mảng (array)
my_array = array.array('i', [1, 2, 3, 4])

# Chuyển đổi mảng thành bytes
bytes_representation = my_array.tobytes()

# Giải mã bytes thành chuỗi UTF-8
string_representation = bytes_representation.decode('utf-8')

# In chuỗi đại diện cho mảng
print("String representation of the array:", string_representation)