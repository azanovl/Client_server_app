import locale

with open('test_file.txt','w') as f_n:
    f_n.write('сетевое окружение''\n''сокет''\n''декоратор')

def_coding = locale.getpreferredencoding()
print(def_coding)
print(f_n)

with open('test_file.txt', 'r') as f_n:
    print(f_n.read())


