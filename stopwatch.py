from time import sleep
import os
import sys
def stopwatch():
    s = int(sys.argv[1])
    while s>=0:
        print(s,' ',end='\r')
        # print(s,sep='')
        sleep(1)
        s -= 1
    os.system('sxiv /home/duy/Pictures/dieu_in_toilet.png')        
    os.system('mpv /home/duy/Music/curtainCall/Eminem\ -\ FACK.mp3')
if __name__ == "__main__":
    stopwatch()
