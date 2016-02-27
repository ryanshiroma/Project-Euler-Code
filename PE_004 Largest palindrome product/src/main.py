'''
Created on Aug 17, 2014

@author: ryanshiroma
'''
import math
import time
def isPal(n):

    for i in range(3):
        first=10**(i)
        second=10**(6-i-1)
        if math.floor(n/first)%10!=math.floor(n/second)%10:
            return False
    return True
found=False
for i in range(999,600,-1):
    for j in range(999,600,-1):
        if found ==False:
            if isPal(i*j)==True:
                found=True
                print(i*j)
                print(i,j)



if __name__ == '__main__':
    pass