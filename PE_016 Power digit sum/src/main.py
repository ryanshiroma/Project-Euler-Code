'''
Created on Aug 18, 2014

@author: ryanshiroma
'''
import time
start = time.time()
a=str(2**1000)
s=0
for i in range(len(a)):
    s+=int(a[i])
print(s)
print((time.time()-start)*1000," milliseconds")

if __name__ == '__main__':
    pass