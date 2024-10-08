import sqlite3

con=sqlite3.connect('Python/join.db')

try:
    con.execute("create table std(no int,name text,age int)")
except:
    print("Table Exists")  

# con.execute("insert into std(no,name,age)values(1,'Anu',21),(2,'Manu',21),(3,'riya',23),(4,'maya',23)")
# con.commit()


try:
    con.execute("create table mark(no int,sub text,mark real)")
except:
    print("Table Exists")  

# con.execute("insert into mark(no,sub,mark)values(1,'phy',70),(2,'phy',71),(3,'phy',93),(4,'python',93),(4,'python',93)")
# con.commit()

# data=con.execute("select std.no, std.name,std.age,mark.sub,mark.mark from std join mark on std.no=mark.no")
# for i in data:
#     print(i)
'''
(1, 'Anu', 21, 'phy', 70.0)
(2, 'Manu', 21, 'phy', 71.0)
(3, 'riya', 23, 'phy', 93.0)
'''    

# data=con.execute("select std.no, std.name,std.age,mark.sub,mark.mark from std left join mark on std.no=mark.no")
# for i in data:
#     print(i)
'''
(1, 'Anu', 21, 'phy', 70.0)
(2, 'Manu', 21, 'phy', 71.0)
(3, 'riya', 23, 'phy', 93.0)
(4, 'maya', 23, None, None)
'''    

# data=con.execute("select std.no, std.name,std.age,mark.sub,mark.mark from std cross join mark ")
# for i in data:
#     print(i)
'''
(1, 'Anu', 21, 'phy', 70.0)
(1, 'Anu', 21, 'phy', 71.0)
(1, 'Anu', 21, 'phy', 93.0)
(1, 'Anu', 21, 'python', 93.0)
(1, 'Anu', 21, 'python', 93.0)
(2, 'Manu', 21, 'phy', 70.0)
(2, 'Manu', 21, 'phy', 71.0)
(2, 'Manu', 21, 'phy', 93.0)
(2, 'Manu', 21, 'python', 93.0)
(2, 'Manu', 21, 'python', 93.0)
(3, 'riya', 23, 'phy', 70.0)
(3, 'riya', 23, 'phy', 71.0)
(3, 'riya', 23, 'phy', 93.0)
(3, 'riya', 23, 'python', 93.0)
(3, 'riya', 23, 'python', 93.0)
(4, 'maya', 23, 'phy', 70.0)
(4, 'maya', 23, 'phy', 71.0)
(4, 'maya', 23, 'phy', 93.0)
(4, 'maya', 23, 'python', 93.0)
(4, 'maya', 23, 'python', 93.0)
'''