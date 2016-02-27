'''
Created on Aug 18, 2014

@author: ryanshiroma
'''
import csv
import time
start=time.time()
tri=[]
srcfile='../p067_triangle.txt'
with open(srcfile, 'rb') as csvfile:
    t = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in t:
        tri.append([int(row[i]) for i in range(len(row))])
    
prods=[[tri[0][0]]]
for i in range(1,len(tri)):
    prods.append([0 for j in range(i+1)])
 
for i in range(1,len(tri)):
    for j in range(i+1):
        if j==0:
            prods[i][j]=prods[i-1][j]+tri[i][j]
        elif j==i:
            prods[i][j]=prods[i-1][j-1]+tri[i][j]
        else:
            prods[i][j]= prods[i-1][j]+tri[i][j] if prods[i-1][j]>prods[i-1][j-1] else prods[i-1][j-1]+tri[i][j]

for i in range(1,len(tri)):
    print(prods[i]) 
          
print(max(prods[i]))
print((time.time()-start)*1000, " milliseconds")

   
if __name__ == '__main__':
    pass