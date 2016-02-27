'''
Created on Aug 17, 2014

@author: ryanshiroma
'''
import time
import math
start=time.time() * 1000

def find(lst, a, b):
    return [i for i, x in enumerate(lst) if x<a or x>b]

cap=120000

list=[0]
for i in range(1,cap):
    list.append(0)
print("done")

for i in range(2,cap):
    if list[i]==0:
        for j in range(2,int(math.floor(cap/i))):
            list[i*j]=1

print(list[1:100])
primes=find(list,1,len(list))
end=time.time() * 1000
print(primes[10002])
print(end-start," milliseconds")

if __name__ == '__main__':
    pass