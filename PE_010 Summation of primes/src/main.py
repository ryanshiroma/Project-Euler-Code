'''
Created on Aug 18, 2014

@author: ryanshiroma
'''
import time
import math
start=time.time() * 1000

def find(lst, a, b):
    return [i for i, x in enumerate(lst) if x<a or x>b]
cap=2000000
lst=[0]
for i in range(cap-1):
    lst.append(0)
print("done")
lst[0]=1
lst[1]=1
for i in range(2,int(math.sqrt(cap))):
    if lst[i]==0:
        print(int(math.floor((cap-1)/(i))),i)
        for j in range(2,int(math.floor((cap-1)/(i)))+1):
            lst[i*j]=1

print(lst[:100])
primes=find(lst,1,len(lst))
end=time.time() * 1000
print(len(primes))
print(primes[:400])
print(sum(primes))
print(primes[-1])
print(end-start," milliseconds")


if __name__ == '__main__':
    pass