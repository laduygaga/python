import os
from time import sleep

f = open('1000PW.txt', 'r')
a = f.readlines()
b = ''.join(a)
c = b.split()
for i in c:
    print(i)
    os.system('echo {}|festival --tts'.format(i))
    sleep(1)
