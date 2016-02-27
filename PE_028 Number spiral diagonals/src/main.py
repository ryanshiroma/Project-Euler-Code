'''
Created on Sep 2, 2014

@author: ryanshiroma
'''

import numpy as np

x=3
y=3
seq=1
move=1
matrix=np.empty([5,5])
while y!=0:
    for j in range(move):
        matrix[y,x]=seq
        x+=1
        seq+=1
    for j in range(move):
        matrix[y,x]=seq
        y+=1
        seq+=1
    move+=1
    for j in range(move):
        matrix[y,x]=seq
        x-=1
        seq+=1
    for j in range(move):
        matrix[y,x]=seq
        y-=1
        seq+=1
for j in range(move+1):
    matrix[y,x]=seq
    x+=1
    seq+=1
print(matrix)
if __name__ == '__main__':
    pass