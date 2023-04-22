#Calculator program
num1=int (input("Enter the first number \t"))
num2=int(input("Enter the second number \t"))
while(True):
    o=int(input("Enter the option \n1:ADD\n2.SUB\n3.MUL\n4.DIV\n5.EXIT\n"))
    if(o==1):
        print("SUM",num1,"+",num2,"=",num1+num2)
    elif(o==2):
        print("DIFF",num1,"-",num2,"=",num1-num2)
    elif(o==3):
        print("PRODUCT",num1,"X",num2,"=",num1*num2)
    elif(o==4):
        print("QUOTIENT",num1,"/",num2,"=",num1/num2)
    elif(o==5):
        break
    else:
        print("INVALID")