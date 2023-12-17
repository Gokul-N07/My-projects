import mysql.connector

from tabulate import tabulate

mydb = mysql.connector.connect(host="localhost",user="root",password="gokul@cse1234567",database="gokul")

c = mydb.cursor()

def add_student():
    id = input("Enter Student id: ")
    while True:
        reg = input("Enter Student Reg.No (6 digit number): ")
        if len(reg)==6 :
            name = input("Enter Student Name: ")
            year = input("Enter College year: ")
            dept = input("Enter Student Department: ")
            sql = "insert into student (Id,Reg_no,Student_name,College_year,Department) values(%s,%s,%s,%s,%s)"
            data =(id,reg,name,year,dept)
            c.execute(sql,data)
            mydb.commit()
            print("Data has been inserted successfully")
            return
        
        else:
            print("Invalid Student Reg.No. Please try again")

def display_all():
    sql = "select Id,Reg_no,Student_name,College_year,Department from student"
    c.execute(sql)
    res = c.fetchall()
    print(tabulate(res,headers=["Id","Reg_no","Student_name","College_year","Department"]))

def select():
    reg = input("Enter student Reg.No(6 digit number): ")
    if len(reg)==6:
        sql = "select Id,Reg_no,Student_name,College_year,Department from student where Reg_no='"+reg+"'"
        c.execute(sql)
        res = c.fetchall()
        print(tabulate(res,headers=["Id","Reg_no","Student_name","College_year","Department"]))
    
    else:
        print("Invalid Reg.No. Please try again")


def update(id,reg,name,clg,dept):
    sql = "update student set Reg_no=%s,Student_name=%s,College_year=%s,Department=%s where Id=%s"
    data =(reg,name,clg,dept,id)
    c.execute(sql,data)
    mydb.commit()
    print("Student Data has been updated successfully")


def delete(id):
    sql = "delete from student where Id=%s"
    data = (id,)
    c.execute(sql,data)
    mydb.commit()
    print("Student data has been deleted successfully ")
        

uname = input("Enter username: ")
pw = input("Enter password: ")
if uname=="admin" and pw=="gokul123":
    print("Welcome admin\n")
    print("Student Database Management\n")
    while True:
        print("1.Add Student Details\n2.Display Student Details\n3.Update Student Details\n4.Delete Student Details\n5.Exit")
        ch = int(input("Enter your choice: "))
        if ch==1:
            add_student()

        elif ch==2:
                print("1.Display All Student Details\n2.Select Student Details")
                ch = int(input("Enter your choice: "))
                if ch==1:
                    display_all()
                elif ch==2:
                    select()
                else:
                    print("Invalid choice...Please try again")

        elif ch==3:
            id = input("Enter student id: ")
            reg = input("Enter Student Reg.no: ")
            name = input("Enter Student name: ")
            clg = input("Enter College year:  ")
            dept = input("Enter Student Department: ")
            update(id,reg,name,clg,dept)

        elif ch==4:
            id = input("Enter Student id: ")
            delete(id)

        elif ch==5:
            break

        else:
            print("Invalid choice...Please try again")
else:
    print("wrong username or password")
