'''
Created on Sep 2, 2014

@author: ryanshiroma
'''
import numpy as np

def add_till(btotal,coin):
    return np.floor((2-btotal)/coin)*coin+btotal

i=0
coins=np.array([0.01,0.02,0.05,0.1,0.2,0.5,1,2])
counts=np.array([0,0,0,0,0,0,0])
for c1 in coins:
    total=0
    coins[::-1]*coins
    total=add_till(total,c1)
    i+=1


print(count)
        

if __name__ == '__main__':
    pass