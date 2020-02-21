import subprocess
import os
from time import sleep

f = open('/home/duy/1000.txt', 'r')
a = f.readlines()
b = ''.join(a)
c = b.split()
for i in c:
    print(c.index(i), i)
    os.system(f'goldendict {i}')
    # subprocess.Popen(f"goldendict  {i}", shell = True)
    sleep(.8)
