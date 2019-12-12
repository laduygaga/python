from string import *
import sys
import time
def f():
    target = 'hello, world'
    begin = [''] * len(target)
    for i, j in enumerate(target): 
        for c in printable: 
            if c == j: 
                begin[i] = c 
                print(f"{''.join(begin[:i+1])}", end='\r') 
                time.sleep(0.1)
                break
f()
