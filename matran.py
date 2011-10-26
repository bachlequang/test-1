import os



matran = raw_input("Nhap ma tran:")
g=[]



def strtoint(x):
    matrix = []
    i=0
    if i< len(x):
        i=i+1
        arrow =map (int,x.replace(' ',''))
        matrix.append(arrow)
    return matrix 

def count(bach):
    i=-1
    args = bach.split(" ")
    for arg in args:
        i=i +1
    return i    

def binhphuong(g):
    i=0
    while i<g:
        i=i+1
        if i * i ==g:
           return True
            

g=strtoint(matran)
x=str(g).replace(" ","")
x=x.strip('[')
x=x.rstrip(']')
x=x.replace(",",' ')
x1=len(x)-count(x)


    
if binhphuong(x1):
    print "ok !"

print x


