from sys import argv

script,argv1,argv2,argv3 = argv
pheptinh = argv2


def tinh(tinh1, tinh3):
    if pheptinh == "+":
        print int(tinh1) + int(tinh3)
    elif pheptinh =="-":
        print int(tinh1) - int(tinh3)
    elif pheptinh =="*":
        print int(tinh1)* int(tinh3)
    elif pheptinh =="/":
        print float(tinh1)/ float(tinh3)
    else:  
        print"Expression errors!"    

tinh(argv1,argv3)
        
    

