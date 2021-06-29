s_1 = 'разработка'
s_2 = 'администрирование'
s_3 = 'protocol'
s_4 = 'standart'

s_1_to_bytes = s_1.encode('utf-8')
s_2_to_bytes = s_2.encode('utf-8')
s_3_to_bytes = s_3.encode('utf-8')
s_4_to_bytes = s_4.encode('utf-8')

s_1_to_bytes_to_str = s_1_to_bytes.decode('utf-8')
s_2_to_bytes_to_str = s_2_to_bytes.decode('utf-8')
s_3_to_bytes_to_str = s_3_to_bytes.decode('utf-8')
s_4_to_bytes_to_str = s_4_to_bytes.decode('utf-8')

print(s_1, s_2, s_3, s_4)
print(s_1_to_bytes, s_2_to_bytes, s_3_to_bytes, s_4_to_bytes)
print(s_1_to_bytes_to_str, s_2_to_bytes_to_str, s_3_to_bytes_to_str, s_4_to_bytes_to_str)
