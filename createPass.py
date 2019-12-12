import os
f = open('/home/duy/gits/python/test/birthday.txt','r')
l = f.readlines()
l1 = ''.join(i for i in l)
l2 = l1.split('\n') 
f.close()
for i in l2:
    os.system("crunch 8 8 0123456789 -t {} -o {}.txt".format(i,i))
