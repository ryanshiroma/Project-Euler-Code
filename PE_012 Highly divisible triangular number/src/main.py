'''
Created on Aug 18, 2014

@author: ryanshiroma
'''
import math
import time
start = time.time()*1000
def factors(n):
    i=1
    fs=[]
    meet=False
    while meet ==False:
        if i>n/i:
            meet=True
        elif n%i==0:
            fs.append(i)
            fs.append(n/i)
        i+=1
    return set(fs)

found=False
i=1
tn=0
while found ==False:
    tn+=i
    lst=[0]
    fs=factors(tn)  
    if len(fs)>500:
        found=True
        print(tn)
        print(len(fs))
    i+=1
print(time.time()*1000-start," milliseconds")
if __name__ == '__main__':
    pass