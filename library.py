import datetime
print(datetime.datetime.now().strftime("%x"))
lib=[]
mem=[]
borrowed_books=[]

while True:
    print('''
1.Add Books
2.View Books          
3.Update Books
4.Remove Books
5.Register or View Members
6.Book (Borrow/Return/Status)
7.Search 
8.Exit                        
       ''')
    choice=int(input("Enter Your Choice :"))
    if choice==1:
        title=input("Book Title :")
        id=int(input("ID :"))
        Category=input("Category :")
        author=input("Author :")
        lan=input("Language :")
        pub=input("Publisher :")
        date=datetime.datetime.now().strftime("%x")
        lib.append([title,id,Category,author,lan,pub,date])
    elif choice==2:
        print('{:<15}{:<10}{:<10}{:<15}{:<10}{:<15}{:<10}'.format('title','id','category','author','lan','pub','date'))    
        print('_'*85)
        for i in lib:
            print('{:<15}{:<10}{:<10}{:<15}{:<10}{:<15}{:<10}'.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    elif choice==3:
        title=input("Book Title :")
        f=0
        for i in lib:
            if i[0]==title:
                f=1
                while True:
                    print('''
1.id
2.Category
3.author
4.language
5.publisher
6.Exit                          
''')
                    sub_ch=int(input("Enter Your Choice For Update :"))
                    if sub_ch==1:
                       new_ID=int(input("ID :"))
                       i[1]=new_ID
                    elif sub_ch==2:
                       new_category=input("Category :")
                       i[2]=new_category  
                    elif sub_ch==3:
                       new_author=input("Author :")
                       i[3]=new_author   
                    elif sub_ch==4:
                       new_lan=input("New Lan :")
                       i[4]=new_lan
                    elif sub_ch==5:
                       new_pub=input("New pub :")
                       i[5]=new_pub   
                    elif sub_ch==6:
                       break
        
        if f==0:
               print('ID Not Found')
    elif choice==4:
        id=int(input("ID :"))
        f=0
        for i in lib:
            if i[1]==id:
                lib.remove(i)
                f=1
        if f==0:
            print("ID Not Found")
    elif choice==5:
                  while True:
                    print('''
1.Register Members
2.View Members 
3.Exit                                               
''')
                    sub_ch=int(input("Enter Your Choice For Update :"))
                    if sub_ch==1:
                       name=input("Full Name :")
                       address=input("Address :")
                       id=int(input("Membership ID :"))
                       date=datetime.datetime.now().strftime("%x")
                       mem.append([name,address,id,date])

                    elif sub_ch==2:
                            print('{:<15}{:<30}{:<10}{:<15}'.format('name','address','id','date'))    
                            print('_'*75)
                            for i in mem:
                                print('{:<15}{:<30}{:<10}{:<15}'.format(i[0],i[1],i[2],i[3]))
                    elif sub_ch==3:
                        break 
    elif choice == 6:
        while True:
            print('''
1. Borrow Book
2. Return Book
3. Check Book Status
4. Exit                                                                  
''')
            sub_ch = int(input("Enter Your Choice: "))
            
            if sub_ch == 1:
                member_id = int(input("Enter Member ID: "))
                f=0
                
                
                for i in mem:
                    if i[2] == member_id:
                        f=1
                        
                
                if f==0:
                    print("Member ID Not Found")
                    

                book_id = int(input("Enter Book ID: "))
                f=0
                
               
                for i in lib:
                    if i[1] == book_id:
                        f=1
                        book_title = i[0]
                        
                
                if f==0:
                    print("Book ID Not Found")
                    
                
                
                borrow_date = datetime.datetime.now().strftime("%x")
                borrowed_books.append([book_title, book_id, member_id, borrow_date])
                print(f"Book '{book_title}' borrowed successfully on {borrow_date}")
            
            elif sub_ch == 2:
                book_id = int(input("Enter Book ID: "))
                f=0
                
                
                for b in borrowed_books:
                    if b[1] == book_id:
                        f=1
                        borrowed_books.remove(b)
                        return_date = datetime.datetime.now().strftime("%x")
                        print(f"Book '{b[0]}' returned successfully on {return_date}")
                        
                
                if f==0:
                    print("Book ID Not Found or Book Not Borrowed")
            
            elif sub_ch == 3:
                book_id = int(input("Enter Book ID: "))
                f=0
                
                
                for b in borrowed_books:
                    if b[1] == book_id:
                        f=1
                        print(f"Book ID {book_id} is borrowed by Member ID {b[2]} on {b[3]}")
                        
                
                if f==0:
                    print("Book ID Not Found or Book Not Borrowed")
            
            elif sub_ch == 4:
                break
    elif choice==7:
         id=int(input('Enter ID :')) 
         f=0
         for i in lib:
            if i[1]==id:
               print(i)
               f=1
         if f==0:
               print('ID Not Found')  
    elif choice==8:
        break
    else:
        print("Invalid Choice")                         
        



                               
                       
        
        
       
         
         
       
         
      






    