'''
Created on Aug 19, 2014

@author: ryanshiroma
'''
n=100
fact=1
for i in range(1,n+1):
    fact*=i
fs=str(fact)
print(fs)
print(sum([int(fs[i]) for i in range(len(fs))]))

if __name__ == '__main__':
    pass