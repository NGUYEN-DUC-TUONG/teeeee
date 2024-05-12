import array

# Mảng ban đầu
char_array = array.array('b', b'hello')

# Chuỗi cần nối vào mảng
new_string = ' world'

# Nối chuỗi vào mảng sử dụng phương thức frombytes()
char_array.frombytes(new_string.encode('utf-8'))

# In mảng kết quả
print("Mảng sau khi nối chuỗi:", char_array)