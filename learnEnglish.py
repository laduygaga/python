from espeakng import ESpeakNG
from time import sleep

f = open('/home/duy/1000PW.txt', 'r')
rl = f.readlines()
a = ESpeakNG()
a.voice = 'en'
for i in rl:
    print(i)
    a.say(i)
    sleep(1)
