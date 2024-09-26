import datetime
print(datetime.datetime.now().strftime("%x"))
ems=[]


while True:
    print('''
1.Registration
2.View Employee Details
3.Update Employee Deatails
4.Delete Employee Deatails
5.Search
6.Add Task
7.View Task
8.Exit                                        
      ''')
    while True:
      try: 
          choice=int(input("Enter Your Choice :"))
          break
      except:
          print("Enter Correct Data")
        #   pass
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
               f=1
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
                       i[2]=new_age
                   elif sub_ch==2:
                       new_salary=int(input("New Salary :"))
                       i[3]=new_salary  
                   elif sub_ch==3:
                       new_position=input("New Position :")
                       i[4]=new_position    
                   elif sub_ch==4:
                       new_experience=int(input("New Experience :"))
                       i[5]=new_experience
                   elif sub_ch==5:
                       break
                          
                       

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
    elif choice==6:
        id=int(input("Enter ID :"))
        f=0
        for i in ems :
            if i[0]==id:
                f=1
                task=input("Enter Task :")  
                date=datetime.datetime.now().strftime("%x")
                i.append([task,date])

        if f==0:
               print('ID Not Found') 
    elif choice==7:
        print('{:<10}{:<10}{:<10}{:<10}'.format('id','name','task','date'))  
        print('_'*50)  
        for i in ems:
            if len(i)>6:
                print('{:<10}{:<10}{:<10}{:<10}'.format(i[0],i[1],i[6][0],i[6][1]))
    elif choice==8:
        break
    else:
        print("Invalid Choice")                          