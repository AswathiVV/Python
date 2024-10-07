import sqlite3

con=sqlite3.connect('Python/sample.db')

try:
    con.execute("create table std(roll_no int,name text,age int,mark real)")
except:
    print("Table Exists")  


# con.execute("insert into std(roll_no,name,age,mark)values(1,'Anu',21,80),(2,'Manu',21,70),(3,'riya',23,78)")
# con.commit()


# roll=int(input("Enter Roll No :"))
# name=input("Enter Name :")
# age=int(input("Enter Age :"))
# mark=float(input("Enter Mark :"))
# con.execute('insert into std(roll_no,name,age,mark)values(?,?,?,?)',(roll,name,age,mark))
# con.commit()



# l=int(input("Limit :"))
# for i in range(l):
#      roll=int(input("Enter Roll No :"))
#      name=input("Enter Name :")
#      age=int(input("Enter Age :"))
#      mark=float(input("Enter Mark :"))
#      con.execute('insert into std(roll_no,name,age,mark)values(?,?,?,?)',(roll,name,age,mark))
#      con.commit()


# data=con.execute('select * from std')
# for i in data:
#     print(i)


# data=con.execute('select * from std')
# for i in data:
#         print('{:<15}{:<10}{:<10}{:<15}'.format('roll_no','name','age','mark'))    
#         print('_'*45)
#         for i in data:
            # print('{:<15}{:<10}{:<10}{:<15}'.format(i[0],i[1],i[2],i[3]))
            
'''
roll_no        name      age       mark           
_____________________________________________
2              Manu      21        70.0           
3              riya      23        78.0           
1              a         20        70.0           
1              w         2         2.0            
1              a         20        70.0           
2              b         23        78.0           
3              c         24        91.0  
'''

# data=con.execute("select * from std where name='riya' ")
# for i in data:
#     print(i)
'''
(3, 'riya', 23, 78.0)
'''    


# roll=int(input('Enter Roll no :')) 
# data=con.execute("select * from std where roll_no=?",(roll,))  
# for i in data:
#     print(i) 
'''
Enter Roll no :3
(3, 'riya', 23, 78.0)
(3, 'c', 24, 91.0)
'''                

# con.execute("update std set name='amal' where name='c' ") 
# con.commit()    
#           
               
# name=input("Old Name :")
# n_name=input("new Name :")
# con.execute("update std set name=? where name=? " ,(n_name,name)) 
# con.commit()              
'''
Old Name :w
new Name :dia
'''            

# con.execute("delete from std where roll_no=1")
# con.commit()
 
# d=int(input("Enter Roll No :"))
# con.execute("delete from std where roll_no=? ",(d,))      
# con.commit() 