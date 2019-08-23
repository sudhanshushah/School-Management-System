from info import *
def x1():
    print("\nThe list of student are:\n")
    j=len(l)
    print("Roll  Name     Math Science English")
    for i in range(0,j):
        print("%s> "%r[i],l[i]," CGPA:%s\n"%m[i])
def x2():
    po=[]
    x=input("\nEnter a new name: ")
    po.append(x)
    y=int(input("\nEnter the roll number: "))
    r.append(y)
    x=float(input("\nEnter Math marks: "))
    po.append(x)
    x=float(input("\nEnter Science marks: "))
    po.append(x)
    x=float(input("\nEnter English marks: "))
    po.append(x)
    l.append(po)
    z=float(input("\nEnter the CGPA: "))
    m.append(z)
    j=len(l)
    print("\nThe list of student now are:\n")
    print("Roll  Name     Math Science English")
    for i in range(0,j):
        print("%s> "%r[i],l[i]," CGPA:%s\n"%m[i])
def x3():
    y=input("\nEnter a name to search: ")
    b=0
    j=len(l)
    for i in range(0,j):
        if(y==l[i][0]):
            b+=1
            break
    if(b==1):
        print("\n",y,"was found in the list!\n")
        print("Roll  Name     Math Science English")
        print("%s> "%r[i],l[i]," CGPA:%s\n"%m[i])
    else:
        print("\nThe name '%s' was not found in the list\n"%y)
def x4():
    y=input("\nEnter a name to be removed: ")
    b=0
    j=len(l)
    for i in range(0,j):
        if(y==l[i][0]):
            b+=1
            break
    if(b==1):
        del(l[i])
        del(r[i])
        del(m[i])
        print("\nThe record of '%s' was deleted\n"%y)
    else:
        print("\nThe name '%s' was not found...\n"%y)
    j=len(l)
    print("\nThe list of student now are:\n")
    print("Roll  Name     Math Science English")
    for i in range(0,j):
        print("%s> "%r[i],l[i]," CGPA:%s\n"%m[i])
