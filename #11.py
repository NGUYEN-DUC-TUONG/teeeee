import array

# Mảng ban đầu
my_array = array.array('i', [1, 2, 3])

# Sử dụng phương thức buffer_info() để lấy thông tin bộ đệm
buffer_info = my_array.buffer_info()

# In thông tin bộ đệm
print("Thông tin bộ đệm:", buffer_info)