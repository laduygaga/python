from string import *
import time
import sys
target = 'FUCK YOU, MOTHER FUCKER!!!'
begin = ''
for i in target:
    for c in printable: 
        sys.stdout.write(f'\r{begin}{c}')
        time.sleep(0.005) 
        if c == i:
            begin += c
            break
