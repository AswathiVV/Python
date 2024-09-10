def number():
        a=int(input("Enter a no.:"))
        b=int(input("Enter a no.:"))
        return a,b
def add():
        a,b=number()
        print(a+b)
def sub():
       a,b=number()
       print(a-b)
def mul():
       a,b=number()
       print(a*b) 
def div():
       a,b=number()
       print(a/b)                     
def mod():
       a,b=number()
       print(a%b)
      
while True:
    print('''
1.add
2.subtract
3.multiplication
4.division
5.modulus 
6.exit                          
''')
    choice=int(input("Enter Your Choice:"))
    if choice==1:
           add()
    elif choice==2:
           sub()
    elif choice==3:
           mul()
    elif choice==4:
           div()       
    elif choice==5:
           mod()
    elif choice==6:
           break       
     

