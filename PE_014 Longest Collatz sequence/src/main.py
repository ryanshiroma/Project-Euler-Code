'''
Created on Aug 18, 2014

@author: ryanshiroma
'''
import time
start=time.time()
max=0
maxi=0
a=0
hash={}
for i in range(1,1000000):
    n=i
    x=1
    while not(n in hash or n==1):      
        if n%2==0:
            n/=2
        else:
            n=3*n+1
        x+=1
    
    if n in hash:
        a+=1
        x+=hash[n]
        hash[i]=x
    else:
        hash[n]=x
    if x>max:
        max=x
        maxi=i
print(maxi,max)
print((time.time()-start)*1000, " milliseconds")        
if __name__ == '__main__':
    pass