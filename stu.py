from func import *
a=1
while(a==1):
    x=int(input("""     Student Management System
Enter 1 : To View Student's List 
Enter 2 : To Add New Student 
Enter 3 : To Search Student 
Enter 4 : To Remove Student 
Enter any other number to exit
    
    """))
    if(x==1):
        x1()
    elif(x==2):
        x2()
    elif(x==3):
        x3()
    elif(x==4):
        x4()
    else:
        a=0
