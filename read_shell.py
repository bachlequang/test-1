#Do em lam tren windows nen khong co file /etc/passwd,o day em tao rieng 1 file la passwd.txt ,sau do lam thu tuc doc tu file vao.
#Em moi chi chay dc phan chay co tham so


import sys

user_name = sys.argv[1]
txt="passwd.txt"
f = open(txt)



def countlinefile(txt):
    with open(txt) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def checkusername(usertxt):
    str1 ="/bin/"
    str2 =":"
    g=g2=countlinefile(txt)

    if len(sys.argv) > 1:
     while g >= 0:
        g=g-1
        readf=f.readline()
        readf=str(readf)
        x=readf.find(usertxt)
        if x !=-1:
            readf2=str(readf)
            x1=readf2.find(str1)
            if x1 != -1: g1=readf2[x1:]
            print "Shell of user",usertxt,":",g1
            break

    else:
     while g2 >= 0:
       g2=g2-1
       readf3=f.readline()
       readf3=str(readf3)
       y=readf3.find(str2)
       if y != -1:
          g3=readf3[:y]
          y1=readf3.find(str1) 
          if y1 != -1: y2=readf3[y1:]          
          print g3,"->",y2

checkusername(user_name)



        

