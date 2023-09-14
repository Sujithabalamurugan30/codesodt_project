import random
letter=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
number=["1","2","3","4","5","6","7","8","9","0"]
symbol=["!","@","#","$","%","^","&","*","-","+","?"]
input1=int(input("how many alphapet you want add in your password:"))
input2=int(input("how many number you want add in your password:"))
input3=int(input("how many symbol you want add in your password:"))
password=[]
for i in range(1,input1+1):
    char=[random.choice(letter)]
    password=password+char
for i in range(1,input2+1):
    char=[random.choice(number)]
    password=password+char
for i in range(1,input3+1):
    char=[random.choice(symbol)]
    password=password+char
# print(password)
#print(''.join(password))
random.shuffle(password)
print(' '.join(password))
