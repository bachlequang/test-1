

#def strtoint(x):
 #   matrix = []
#    i=0
#    if i< len(x):
#        i=i+1
#        arrow =map (int,x.replace(' ',''))
#        matrix.append(arrow)
 #   return matrix 


#def count(bach):
#    i=-1
 #   args = bach.split(" ")
#    for arg in args:
#        i=i +1
#    return i 
    
#g=strtoint(matran)
#print g
#x=str(g).replace(" ","")
#x=x.strip('[')
#x=x.rstrip(']')
#x=x.replace(",",' ')
#x1=len(x)-count(x)
#print x1
#f binhphuong(x1):
  #  print "Day dung la ma tran N * N"
#else:
 #   print "Day k phai la ma tran N*N"
        
#def binhphuong(g):
 #   i=0
  #  while i<g:
   #     i=i+1
   #     if i * i ==g:
     #      return True

from __future__ import print_function
import math

matran = raw_input("Nhap ma tran:")

def empty_matrix(n):
    m=[]
    for i in range(n):
        m.append([0])
        for j in range(n-1):
            m[i].append(0)
            

def make_matrix(n,m):
    matrix=[]
    empty_matrix(n)
    l=0
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(m[l])
            l+=1
    return matrix
    
matrix1=[]
count = matran.split(" ")
n1 = int(math.sqrt(len(count)))
matrix1 = make_matrix(n1,count)
tong=0

for i in range(n1):
    tong=tong+float(matrix1[i][i])
print (tong)

tong1=0
for j in range(n1):
    tong1=tong+float(matrix1[n1-j-1][j])
    
print (tong1)

for i in range(n1):
    for j in range(n1):
        #if (int(matrix1[i][j] % 2) == 0) and (matrix1[i][j] > 0):  
        if (float(matrix1[i][j]) % 2) ==0 and (float(matrix1[i][j]) >0) :
            pass
        else:
                matrix1[i][j]="x"
        print('{0:>4}'.format(str(matrix1[i][j])), end='')

    print ("")




































