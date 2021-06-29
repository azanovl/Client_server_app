s_1 = 'разработка'
s_2 = 'сокет'
s_3 = 'декоратор'
print(type(s_1), type(s_2), type(s_3))

s_1_bytes = b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
s_2_bytes = '\u0441\u043e\u043a\u0435\u0442'
s_3_bytes = b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80'
print(type(s_1_bytes), type(s_2_bytes), type(s_3_bytes))

s_1_bytes_to_str = bytes.decode(s_1_bytes, encoding='utf-8')
s_2_bytes_to_str = s_2_bytes.encode('utf-16').decode('utf-16')
s_3_bytes_to_str = s_3_bytes.decode('utf-8')
print(s_1_bytes_to_str)
print(s_2_bytes_to_str)
print(s_3_bytes_to_str)