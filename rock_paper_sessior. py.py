#rock 0
#paper 1
#sesior 2
#0==0 draw
#0==1 comp
#0==2 user
#1==0 user
#1==1 draw
#1==2 comp
#2==0 comp
#2==1 user
#2==2 draw
import random
user=int(input("enter your choice\n0.rock\n1.paper\n2.sesior\n"))
computer=random.randint(0,2)
print(computer)
if user == computer:
    print("match drw")
elif user == 2 and computer == 0:
    print("you win")
elif user == 0 and computer == 2:
    print("you lose")
elif user > computer:
    print("you win")
elif computer > user:
    print("you lose")
else:
    print("enter correct number")