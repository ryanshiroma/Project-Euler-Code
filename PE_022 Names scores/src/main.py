'''
Created on Aug 19, 2014

@author: ryanshiroma
'''
import csv
import time
start=time.time()

srcfile='../p022_names.txt'
with open(srcfile, 'rb') as csvfile:
    t = csv.reader(csvfile, quotechar='"')
    for row in t:
        names=row
all=0
sortn=sorted(names)
names=sortn
for i in range(len(names)):
    nme=0
    for j in range(len(names[i])):
        nme+=ord(names[i][j])-64
        print(names[i][j],ord(names[i][j])-64)
    print(nme*(i+1))
    all+=nme*(i+1)
    
print(all)
if __name__ == '__main__':
    pass