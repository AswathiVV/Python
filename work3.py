mem=[{'id':101,'email':'a.gmail','name':'asdff','address':'dfgj','dob':'12/12/12','phone':123,'password':'123','books':[]}]
bk=[{'bk_id':100,'bk_name':'wolf','stock':10,'price':500}]
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
        mem.append({'id':id,'email':email,'name':name,'address':address,'dob':dob,'phone':phone,'password':password,'books':[]})
        print('REGISTRATION SUCCESSFULL')

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
    if f==0:
        print("INVALID USERNAME OR PASSWORD")     
        
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
    print('{:<10}{:<10}{:<10}{:<10}'.format('bk_id','bk_name','stock','price'))  
    print('_'*60)
    for i in bk:
        print('{:<10}{:<10}{:<10}{:<10}'.format(i['bk_id'],i['bk_name'],i['stock'],i['price'])) 
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
def view_users():
     print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('id','email','name','address','dob','phone'))  
     print('_'*100)
     for i in mem:
         print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(i['id'],i['email'],i['name'],i['address'],i['dob'],i['phone']))

def view_profile(user):
    # print(user)
    print('{:<10}{:<20}{:<15}{:<30}{:<10}{:<10}'.format('id','email','name','address','dob','phone','password'))  
    print('_'*100)
    print('{:<10}{:<20}{:<15}{:<30}{:<10}{:<10}'.format(user['id'],user['email'],user['name'],user['address'],user['dob'],user['phone'],user['password']))

def borrow_book(user):
    id = int(input("Enter Book ID: "))
    f=0        
                
    for i in bk:
     if i['bk_id'] == id:
                f=1
                if i['stock']>0:
                    user['books'].append(i['bk_id'])
                    i['stock']-=1
                    print('BOOK BORROWED SUCCESSFULLY')

                else:
                    print("OUT OF STOCK")
    if f==0:
        print('INVALID BOOK ID')  
def return_book(user):
    id = int(input("Enter Book ID: "))
    f=0  

                
    for i in bk:
     if i['bk_id'] == id and id in user['books']:
                f=1
                i['stock']+=1
               
                user['books'].remove(id)
                   
                print('BOOK RETURNED SUCCESSFULLY')

               
    if f==0:
        print('INVALID BOOK ID')  

# def book_in_hand(user):
    
    
        

                        
                
            
  



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
                elif sub_ch==5:
                    view_users()
                              



        elif f==2:# user login
            while True:
                print('''
1.VIEW PROFILE
2.VIEW BOOKS
3.BORROW BOOK
4.RETURN BOOK
5.BOOKS IN HAND
6.EXIT
''')
                sub_ch=int(input("ENTER YOUR CHOICE :"))
                if sub_ch==1:
                    view_profile(user)
                elif sub_ch==2:
                    view_book() 
                elif sub_ch==3:
                    borrow_book(user)
                elif sub_ch==4:
                    return_book(user)
                # elif sub_ch==5:
                #     book_in_hand()     
                elif sub_ch==6:
                    break  
                else :
                    print("INVALID CHOICE")     


            
            
                    
                    


                  
        # else:
        #     print("Invalid Choice") 

            
        

    elif choice==3:
        break    
    else:
        print("INVALID")