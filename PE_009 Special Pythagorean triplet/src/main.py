'''
Created on Aug 18, 2014

@author: ryanshiroma
'''
import time
import math
start=time.time()*1000
sum=0
for a in range(1,500):
    for b in range(a,1000):
        sum=a**2 + b**2
        c=1000-(a+b)
        if a**2+b**2==c**2:
            found =True
            print(a,b,c)
            print(a*b*c)


print(time.time()*1000-start," milliseconds")
if __name__ == '__main__':
    pass