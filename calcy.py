x=int(input("enter the value of 1st number:"))
y=int(input("enter the value of 2nd number:"))
choice=input("what operation you want to perform option are given below \n(+) \n(-) \n(*) \n(/) \nchoose one above operator: ")

def add(x,y):
    c=x+y
    print("the addtion value is:",c)
def sub(x,y):
    c=x-y
    print("the subtraction value is:",c)
def mul(x,y):
    c=x*y
    print("the multiplication value is:",c)
def div(x,y):
    c=x/y
    print("the division value is:",c)
if choice=="+":    
    add(x,y)
elif choice=="-":
    sub(x,y)
elif choice=="*":
    mul(x,y)
elif choice=="/":
    div(x,y)
else:
    print("please choose a correct operator")

