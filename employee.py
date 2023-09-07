from os import system
import re
import mysql.connector

'''con = mysql.connector.connect(host="localhost", user="root", password="050902")
cursorObject = con.cursor()
cursorObject.execute("CREATE DATABASE Project")'''

con=mysql.connector.connect(host="localhost", user="root", password="050902",database="Project")
cursorObject=con.cursor()
'''cursorObject.execute("CREATE TABLE employee_data(Id INT(11) PRIMARY KEY,Name VARCHAR(1800),Email_Id TEXT(1800),Phone_no BIGINT(11),Address TEXT(1000),Post TEXT(1000),Salary BIGINT(20))")'''


regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}\b'
pattern = re.compile("(0|91)?[7-9][0-9]{9}")


def add_employee():
    print("{:>60}".format("-->Add Employee Record<<--"))
    Id = input("Enter Employee Id:")
    if(check_employee(Id) == True):
        print("Employee Id already exists\nTry again")
        press = input("Press any key to continue..")
        menu()
    else:
        Name = input("enter employee name:")
        Email_Id = input("Enter Employee Email Id:")
        if(re.fullmatch(regex, Email_Id)):
            print("Valid Email")
        else:
            print("Invalid email")
            press = input("Press any key to continue..")
            menu()
        Phone_no = input("enter employee phone no:")
        if(pattern.match(Phone_no)):
            print("Valid phone number")
        else:
            print("Invalid phone number")
            press = input("Press any key to continue")
            menu()
    Address = input("Enter employee address:")
    Post = input("Enter employee post")
    Salary = input("Enter employee salary")
    data = (Id, Name, Email_Id, Phone_no, Address, Post, Salary)
    sql = 'Insert into employee_data values(%s,%s,%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Successfully Added Employee Record")
    press = input("Press any key  to continue")
    menu()


def check_employee_name(employee_name):
    sql = 'select * from employee_data where Name=%s'
    c = con.cursor(buffered=True)
    data = (employee_name)
    c.execute(sql, data)
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False


def check_employee(employee_id):
    sql = 'select * from employee_data where Id=%s'
    c = con.cursor(buffered=True)
    data = (employee_id,)
    c.execute(sql, data)
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False


def display_employee():
    print("{:>60}".format("-->Display Employee Record<<--"))
    sql = 'select * from employee_data'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        print("Employee Id:",i[0])
        print("Employee Name:", i[1])
        print("Employee Email Id:", i[2])
        print("Employee Phone no:", i[3])
        print("Employee Address:", i[4])
        print("Employee Post:", i[5])
        print("Employee Salary:", i[6])
        print("\n")
    press = input("Press any key to continue")
    menu()


def update_employee():
    print("{:>60}".format("-->> Update Employee Record<<--"))
    Id = input("Enter Employee Id:")
    if (check_employee(Id) == False):
        print("Employee record not exists \nTry again")
        press = input("Press any key to continue")
        menu()
    else:
        Email_Id = input("Enter Employee Email Id:")
        if (re.fullmatch(regex, Email_Id)):
            print("Valid email")
        else:
            print("Invalid email")
            press = input("Press any key to continue")
            update_employee()
        Phone_no = input("Enter Employee Phone Number:")
        if (pattern.match(Phone_no)):
            print("Valid phone number")
        else:
            print("Invalid phone number")
            press == input("Press any key to continue")
            update_employee()
        Address = input("Enter Employee Address:")
        sql = 'update employee_data set Email_Id=%s,Phone_no=%s,Address=%s where Id=%s'
        data = (Email_Id, Phone_no, Address, Id)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Updated Employee Record")
        press = input("Press any key to continue")
        menu()


def promote_employee():
    print("{:>60}".format("-->>promote employee record<<--"))
    Id = input("Enter Employee Id:")
    if(check_employee(Id) == False):
        print("Employee record not exists\nTry again")
        press = input("Press any key to continue")
        menu()
    else:
        Amount = int(input("Enter increase salary:"))
        sql = 'select salary from employee_data where Id=%s'
        data=(Id,)
        c = con.cursor()
        c.execute(sql, data)
        r = c.fetchone()
        t = r[0] + Amount
        sql = 'update employee_data set Salary=%s where Id=%s'
        d = (t, Id)
        c.execute(sql, d)
        con.commit()
        print("Employee Promoted")
        press = input("Press any key to continue")
        menu()
def remove_employee():
    print("{:>60}".format("-->>Remove Employee Record<<--"))
    Id = input("enter employee Id:")
    if(check_employee(Id) == False):
        print("Employee record not exists\nTry again")
        press = input("Press any key to continue")
        menu()
    else:
        sql = 'delete from employee_data where Id=%s'
        data=(Id,)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Employee removed")
        press = input("Press any key to continue")
        menu()
def search_employee():
    print("{:>60}".format("-->>Search Employee Record<<--"))
    Id = input("Enter Employee Id:")
    if(check_employee(Id) == False):
        print("Employee record not exists\nTry again")
        press = input("Press any key to continue")
        menu()
    else:
        sql = 'select * from employee_data where Id=%s'
        data=(Id,)
        c = con.cursor()
        c.execute(sql,data)
        r = c.fetchall()
        for i in r:
            print("Employee Id:",i[0])
            print("Employee Name:", i[1])
            print("Employee Email Id:", i[2])
            print("Employee Phone no:", i[3])
            print("Employee Address:", i[4])
            print("Employee Post:", i[5])
            print("Employee Salary:", i[6])
            print("\n")
        press = input("Press any key to continue")
        menu()
def menu():
    system("cls")
    print("{:>60}".format("********************"))
    print("{:>60}".format("-->> Employee Management System<<--"))
    print("{:>60}".format("********************"))
    print("1.Add Employee Record")
    print("2.Display Employee Record")
    print("3.Update Employee Record")
    print("4.Promote Employee Record")
    print("5.Remove Employee Record")
    print("6.Search Employee Record")
    print("7.Exit\n")
    print("{:>60}".format("-->> Choice Options:[1/2/3/4/5/6/7]<<--"))
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        system("cls")
        add_employee()
    elif ch==2:
        system("cls")
        display_employee()
    elif ch==3:
        system("cls")
        update_employee()
    elif ch==4:
        system("cls")
        promote_employee()
    elif ch==5:
        system("cls")
        remove_employee()
    elif ch==6:
        system("cls")
        search_employee()
    elif ch==7:
        system("cls")
        print("{:>60}".format("Have A Nice Day:"))
        menu()
menu()











