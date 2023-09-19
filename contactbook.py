import sqlite3
conn=sqlite3.connect("contact.db")
print("connection established")
def create():
    conn.execute("""CREATE TABLE CONTACT (NAME TEXT NOT NULL,NUMBER INT NOT NULL)""")

def insert():
    cname=str(input("enter contact name:")).lower()
    cnumber=int(input(f"enter the {cname} phonenumber:"))
    conn.execute(f"INSERT INTO CONTACT(NAME,NUMBER)VALUES('{cname}',{cnumber})")
    conn.commit()

def update(num,nam):
    conn.execute(f"UPDATE CONTACT SET NUMBER= {num} WHERE NAME='{nam}'")
    conn.commit()

def read():
    cursor=conn.execute("SELECT NAME,NUMBER FROM CONTACT")
    for row in cursor:
        print(f"{row[0]}:{row[1]}")
def delete(nam):
    conn.execute(f"DELETE FROM CONTACT WHERE NAME='{nam}'")
    print(f"{nam}the contact details are deleted")
def search(sea):
    print("likely the contact details\n")
    cursor=conn.execute(f"SELECT * FROM CONTACT WHERE NAME LIKE'%{sea}%'")
    for row in cursor:
        print(f"{row[0]} :{row[1]}")
con=True
while con:
    inputs=int(input("1.insert\n2.delete\n3.update\n4.read\n5.search\n"))
    if inputs==1:
        insert()
    elif inputs==2:
        nam=str(input("enter the name to delete contact details:"))
        delete(nam)
    elif inputs==3:
        nam=str(input("enter the name to update contact details:"))
        num=str(input("enter the number to update contact details:"))
        update(num,nam)
    elif inputs==4:
        read()
    elif inputs==5:
        sea=str(input("enter the name to likely contact details:"))
        search(sea)
    else:
        con=False
conn.close()

