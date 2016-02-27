'''
Created on Aug 16, 2014

@author: ryanshiroma
'''


def bran(a):
    print(a)
    for i in range(2,1000000):
        if a%i==0:
            print(a/i,i)
            bran(int(a/i))
            break
            

a=600851475143  
bran(a)

if __name__ == '__main__':
    pass