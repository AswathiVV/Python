emp=[]

def login():
    uname=input("Enter User Name :")
    pword=input("Enter User Password :")
    f=0
    if uname=='admin' and pword=='admin':
        f=1
        return f
def add_emp():
    id=int(input("Enter Your ID :"))
    f1=0
    for i in emp:
        if i['id']==id:
            f1=1
            print("ID EXIT")
            add_emp()
    if f1==0:
        name=input("Enter Your Name :")  
        age=int(input("Enter Your Age :"))  
        salary=int(input("Enter Your Salary :"))
        place=input("Enter Your Place :")
        dob=input("Enter Your DOB :")
        emp.append({'id':id,'name':name,'age':age,'salary':salary,'place':place,'dob':dob}) 
        print(emp)
def update_emp():
    id=int(input("Enter Your ID :"))
    f1=0
    for i in emp:
        if i['id']==id:
            f1=1
            name=input("Enter Your Name :")  
            age=int(input("Enter Your Age :"))  
            salary=int(input("Enter Your Salary :"))
            place=input("Enter Your Place :")
            dob=input("Enter Your DOB :")
            i['name']=name
            i['age']=age
            i['salary']=salary
            i['place']=place
            i['dob']=dob
    if f1==0:
        print("INVALID ID")    
def delete_emp():
     id=int(input("Enter Your ID :"))
     f1=0
     for i in emp:
        if i['id']==id:
            f1=1
            emp.remove(i)
     if f1==0:
         print("INVALID ID")
def display():
     print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('id','name','age','salary','place','dob'))  
     print('_'*60)
     for i in emp:
        print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(i['id'],i['name'],i['age'],i['salary'],i['place'],i['dob']))

               

while True:
    print('''
1.LOGIN
2.EXIT          
''')    
    choice=int(input("Enter Your Choice :"))
    if choice==1:
        f=login()
        if f==1:
            print('''
1.ADD EMP
2.UPDATE EMP
3.DELETE EMP
4.DISPLAY
5.LOGOUT                   
''')
            sub_choice=int(input("Enter Your Choice :"))
            if sub_choice==1:
                add_emp()
            elif sub_choice==2:
                update_emp() 
            elif sub_choice==3:
                delete_emp()
            elif sub_choice==4:
                display()
            elif choice==5:
                break    
                                
        elif f==0:
            print('INVALID USERNAME OR PASSWORD')
    elif choice==2:
        break
    else:
        ("INVALID CHOICE")        
            
      
                