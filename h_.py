import sys
import time
import string
import random

target = 'FUCK YOU, MOTHER FUCKER!!!'
guess = ['']*len(target)
charlist = string.ascii_letters + string.punctuation + " "
while True:
    guess = [t if c == t else random.choice(charlist) for c, t in zip(guess, target)]
    sys.stdout.write(f'\r{"".join(guess)}')
    sys.stdout.flush()
    time.sleep(0.03)
    if ''.join(guess) == target:
        break

time.sleep(0.2)
print('\n\nACCESS GRANTED')
