import subprocess
import locale

def_coding = locale.getpreferredencoding()
print(def_coding)

args_ya = ['ping', 'yandex.ru']
args_you = ['ping', 'youtube.com']

subproc_ping_ya = subprocess.Popen(args_ya, stdout=subprocess.PIPE)
subproc_ping_you = subprocess.Popen(args_you, stdout=subprocess.PIPE)

for line in subproc_ping_ya.stdout:
    print(line.decode('cp866').encode('utf-8').decode('utf-8'))


for line in subproc_ping_you.stdout:
    print(line.decode('cp866').encode('utf-8').decode('utf-8'))

