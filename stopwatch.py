import time, keyboard
def f(): 
   start = time.time() 
   while True: 
       print(f'{time.time() - start:.2f}', end = '\r') 
       if keyboard.is_pressed('r'): 
           input('press enter to restart ')
           start = time.time() 
       if keyboard.is_pressed('p'): 
           start = time.time() - start
           input('press enter to resume ')
           start = time.time() - start
       if keyboard.is_pressed('q'): 
           break 
f() 
