ems=[]
while True:
    print('''
1.Registration
2.View Employee Details
3.Update Employee Deatails
4.Delete Employee Deatails
5.Search
6.Add Task                    
      ''')
    choice=int(input("Enter Your Choice :"))
    if choice==1:
        id= int(input("Enter id :"))
        name=input("Enter Name :")
        age= int(input("Enter Age :"))
        salary=int(input("Enter Salary :"))
        position=input("Enter Your Position: ")
        experience=int(input("Enter Your experience : "))
        ems.append([id,name,age,salary,position,experience])
    elif choice==2:
        print('{:<10}{:<10}{:<5}{:<10}{:<10}{:<5}'.format('id','name','age','salary','position','experience'))  
        print('_'*50)  
        for i in ems:
            print('{:<10}{:<10}{:<5}{:<10}{:<10}{:<5}'.format(i[0],i[1],i[2],i[3],i[4],i[5]))
    elif choice==3:
         id=int(input('Enter Your id :')) 
         f=0
         for i in ems:
            if i[0]==id:
               age=int(input("Enter Your Age :"))
               salary=int(input("Enter Your Salary :"))
               position=input("Enter Your Position :")
               experience=int(input("Enter Your Experience :")) 
               i[2]=age
               i[3]=salary
               i[4]=position
               i[5]=experience
               f=1
         if f==0:
               print('ID Not Found')           
    elif choice==4:
         id=int(input('Enter Your ID :')) 
         f=0
         for i in ems:
            if i[0]==id:
               ems.remove(i)
               f=1
         if f==0:
               print('ID Not Found')
    elif choice==5:
         id=int(input('Enter Your ID :')) 
         f=0
         for i in ems:
            if i[0]==id:
               print(i)
               f=1
         if f==0:
               print('ID Not Found')            