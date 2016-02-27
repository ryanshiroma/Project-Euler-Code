'''
Created on Aug 17, 2014

@author: ryanshiroma
'''
s=1
for i in range(1,21):
    s*=i
divi=True
for k in range(2,21):
    while divi==True:
        print(s)
        s/=k
        for j in range(1,21):
            if s%j!=0:
                divi=False
    s*=k
    print(s)
    divi=True

if __name__ == '__main__':
    pass