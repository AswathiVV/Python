import sqlite3

con=sqlite3.connect('Python/sample.db')

try:
    con.execute("create table std(roll_no int,name text,age int,mark real)")
except:
    print("Table Exists")  


con.execute("insert into std(roll_no,name,age,mark)values(1,'Anu',21,80),(2,'Manu',21,70),(3,'riya',23,78)")
con.commit()