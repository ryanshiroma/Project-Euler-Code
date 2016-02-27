'''
Created on Aug 16, 2014

@author: ryanshiroma
'''

def fib(a,b,s):
    if b%2==0:
       s+=b
    c=a
    a=b
    b=c+b
    if a>4000000:
        print(a, b)
        print("answer: ",s)
    else:  
        print(a)
        return fib(a,b,s)

fib(0,1,0)
a=0
b=1
s=0
while b<4000000:
    if b%2==0:
        s+=b
    c=a
    a=b
    b=c+b   
print(s)
if __name__ == '__main__':
    pass