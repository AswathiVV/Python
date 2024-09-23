import numbers
import add as c
from sub import sub
from division import*
from multi import *
from floordiv import floordiv

while True:
    print('''
1.Add
2.Subtract
3.division   
4.Multiplication
5.Floor Division                                 
''')
    ch=int(input("Enter Your Choice :"))
    if ch==1:
        a,b=numbers.num()
        c.add(a,b)
    elif ch==2:
        a,b=numbers.num()
        sub(a,b)
    elif ch==3:
        a,b=numbers.num()
        division(a,b)    
    elif ch==4:
        a,b=numbers.num()
        multi(a,b)
    elif ch==5:
        a,b=numbers.num()
        floordiv(a,b)    


        
        


        

