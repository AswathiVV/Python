import sqlite3

con=sqlite3.connect('Python/emp_database.db')

try:
    con.execute("create table emp(id int,name text,age int,salary real,position text,experience int)")
except:
    print("Table Exists")  
emp=[]
while True:
    print('''
1.ADD
2.UPDATE
3.VIEW
4.DELETE
5.SEARCH                                        
''')
    choice=int(input("ENTER YOUR CHOICE :"))
    if choice==1:
        id= int(input("Enter id :"))
        name=input("Enter Name :")
        age= int(input("Enter Age :"))
        salary=int(input("Enter Salary :"))
        position=input("Enter Your Position: ")
        experience=int(input("Enter Your experience : "))
        con.execute('insert into emp(id,name,age,salary,position,experience)values(?,?,?,?,?,?)',(id,name,age,salary,position,experience))
        con.commit()
    elif choice==3:
        # print('{:<10}{:<10}{:<5}{:<10}{:<10}{:<5}'.format('id','name','age','salary','position','experience'))  
        # print('_'*50)  
        # for i in emp:
        #     print('{:<10}{:<10}{:<5}{:<10}{:<10}{:<5}'.format(i[0],i[1],i[2],i[3],i[4],i[5]))
        data=con.execute('select * from std')
#       for i in data:
#           print('{:<15}{:<10}{:<10}{:<15}'.format('roll_no','name','age','mark'))    
#           print('_'*45)
#           for i in data:
             # print('{:<15}{:<10}{:<10}{:<15}'.format(i[0],i[1],i[2],i[3]))

