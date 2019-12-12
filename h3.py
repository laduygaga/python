from string import *
import time
target = 'FUCK YOU, MOTHER FUCKER!!!'
begin = ['*']*len(target)
for i,j in enumerate(target):
    for c in printable: 
        begin[i] = c
        print(f"{''.join(begin)}",end='\r')
        time.sleep(0.005) 
        if c == j:
            break
print('\n')
