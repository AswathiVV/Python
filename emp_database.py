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
6.EXIT                                                
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
    elif choice==2:
                id=int(input('Enter Your id :')) 
                # f=0
                # for i in emp:
                #  if i[0]==id:
                #   f=1
                while True:
                   print('''
1.Age
2.Salary
3.Position 
4.Experience
5.Exit       
 ''')
                   sub_ch=int(input("Enter Your Choice For Update :"))
                   if sub_ch==1:
                       new_age=int(input("New Age :"))
                       con.execute("update emp set age=? where id=? " ,(new_age,id)) 
                       con.commit()  
                   elif sub_ch==2:
                       new_salary=int(input("New Salary :"))
                       con.execute("update emp set salary=? where id=? " ,(new_salary,id)) 
                       con.commit()  
                       
                   elif sub_ch==3:
                       new_position=input("New Position :")
                       con.execute("update emp set position=? where id=? " ,(new_position,id)) 
                       con.commit()  
                        
                   elif sub_ch==4:
                       new_experience=int(input("New Experience :"))
                       con.execute("update emp set experience=? where id=? " ,(new_experience,id)) 
                       con.commit()  
                   elif sub_ch==5:
                       break
        
    elif choice==3:
        data=con.execute('select * from emp')
        print('{:<10}{:<10}{:<5}{:<10}{:<10}{:<5}'.format('id','name','age','salary','position','experience'))  
        print('_'*50)  
        for i in data:
                 print('{:<10}{:<10}{:<5}{:<10}{:<10}{:<5}'.format(i[0],i[1],i[2],i[3],i[4],i[5]))
    
    elif choice==4:
        id= int(input("Enter id :"))
        con.execute("delete from emp where id=? ",(id,))      
        con.commit() 
        print("ID REMOVED")
    elif choice==5:
        id=int(input("Enter Your ID :"))   
        data=con.execute("select * from emp where id=? ",(id,))  
        for i in data:
            print(i)
    elif sub_ch==6:
                break   
    else:
         print("INVALID CHOICE")     
           

            

