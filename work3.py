mem=[]
bk=[]
def register():
    if len(mem)==0:
        id=101
    else:
        id=mem[-1]['id']+1
    print(id)
    email=input("Enter email :") 
    f1=0
    for i in mem:
        if i['email']==email:
            f1=1
            print("ID EXIT")
            register()  
    if f1==0:             
        name=input("Enter User Name :")
        address=input("Enter Address :")
        dob=input("DOB:")
        phone=int(input("Enter Phone no. :"))
        password=input("Password :")
        mem.append({'id':id,'email':email,'name':name,'address':address,'DOB':dob,'phone':phone,'password':password})
        print(mem)

def login():
    uname=input("USER NAME :")
    password=input("PASSWORD :")
    f=0
    if uname =='admin' and password=='admin':
        f=1
    user=' '    
    for i in mem:    
        if uname==i['email'] and password==i['password']:
         f=2
         user=i
        
    return f,user


def add_book():
     if len(bk)==0:
        id=101
     else:
        id=bk[-1]['id']+1
     print(id)
     name=input("Enter Name :")
     stock=input("Stock :")
     price=int(input("Price :"))
     bk.append({'id':id,'name':name,'stock':stock,'price':price})
     print(bk)
def view_book():
    print('{:<10}{:<10}{:<10}{:<10}'.format('id','name','stock','price'))  
    print('_'*60)
    for i in bk:
        print('{:<10}{:<10}{:<10}{:<10}'.format(i['id'],i['name'],i['stock'],i['price'])) 
def update_book():
    id=int(input("Enter Your ID :"))
    f1=0
    for i in bk:
        if i['id']==id:
            f1=1
            name=input("Enter Your Name :")  
            stock=int(input("Stock :"))  
            price=int(input("Price :"))
            i['name']=name
            i['stock']=stock
            i['price']=price
            print("UPDATED SUCCESSFULLY")
           
    if f1==0:
        print("INVALID ID") 

def delete_book():   
     id=int(input("Enter Your ID :"))
     f1=0
     for i in bk:
        if i['id']==id:
            f1=1
            bk.remove(i)
            print("ID REMOVED SUCCESSFULLY")
     if f1==0:
         print("INVALID ID")          

  



while True:
    print('''
1.REGISTRATION          
2.LOGIN
3.EXIT          
''')    
    choice=int(input("Enter Your Choice :"))
    if choice==1:
       
        register()  
    elif choice==2:
        f,user= login()
        if f==1:
            while True:
                print('''
1.ADD BOOK         
2.VIEW BOOK
3.UPDATE BOOK
4.DELETE BOOK
5.VIEW USERS                                       
''')       
                sub_ch=int(input("Enter Your Choice :"))        
                if sub_ch==1: 
                    add_book()
                elif sub_ch==2:
                    view_book()  
                elif sub_ch==3:  
                    update_book()  
                elif sub_ch==4:
                    delete_book()
                elif sub_ch==4:
                    print(mem)           



        # elif f==2:
                    
                    


                  
        # else:
        #     print("Invalid Choice") 

            
        

    # elif choice==3:
    #     break    