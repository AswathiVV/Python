import datetime
lib=[]
user=[{'id':100}]
while True:
    print('''
1.login
2.Exit          
    ''')
    choice=int(input("ENTER YOUR CHOICE :"))
    if choice==1:
      id=int(input("USER ID :"))
      f=0
      for i in user:
            if i['id']==id: 
                f=1
                while True:
                    print('''
            1.Add Book
            2.Update Book
            3.Remove Book
            4.View All Books
            5.Search Books
            6.Exit
                ''')
                    choice=int(input("ENTER YOUR CHOICE :"))
                    if choice==1:
                        title=input("BOOK TITLE :")
                        id=int(input("BOOK ID :"))
                        category=input("CATEGORY :")
                        author=input("AUTHOR :")
                        lan=input("LANGUAGE :")
                        pub=input("PUBLISHER :")
                        date=datetime.datetime.now().strftime("%x")
                        lib.append({'title':title,'id':id,'category':category,'author':author,'lan':lan,'pub':pub,'date':date})
                    elif choice==2:
                        title=input("BOOK TILE :")   
                        f=0
                        for i in lib:
                            if i['title']==title :
                                f=1
                                while True:
                                    print('''
            1.id
            2.language
            3.publisher
            4.Exit                          
            ''')
                                    sub_ch=int(input("Enter Your Choice For Update :"))
                                    if sub_ch==1:
                                        new_id=int(input("NEW ID :"))
                                        i['id']=new_id
                                    elif sub_ch==2:
                                        new_lan=input("LANGUAGE :")   
                                        i['lan']=new_lan
                                    elif sub_ch==3:
                                        new_pub=input("NEW PUBLISHER :")    
                                        i['pub']=new_pub
                                    elif sub_ch==4:
                                        break
                        if f==0:
                         print('ID Not Found') 
                    elif choice==3:
                        id=int(input("ENTER ID :")) 
                        f=0
                        for i in lib:
                            if i['id']==id:
                                lib.remove(i) 
                                f=1
                                print("BOOK REMOVED SUCCESSFULLY")
                        if f==0:
                            print("ID Not Found")
                                    
                    elif choice==4:
                        print('{:<15}{:<10}{:<10}{:<15}{:<10}{:<15}{:<10}'.format('title','id','category','author','lan','pub','date'))    
                        print('_'*85)
                        for i in lib:
                            print('{:<15}{:<10}{:<10}{:<15}{:<10}{:<15}{:<10}'.format(i['title'],i['id'],i['category'],i['author'],i['lan'],i['pub'],i['date']))
                
                    elif choice==5:
                        id=int(input('Enter ID :')) 
                        f=0
                        for i in lib:
                            if i['id']==id:
                              print(i)
                            f=1
                        if f==0:
                            print('ID Not Found')  
                    elif choice==6:
                        break
                    else:
                        print("Invalid Choice")          
               
      if f==0:
                print("ID Not Found")                  
    elif choice==2:
        break
    else:
        print("Invalid Choice") 

    

                           


