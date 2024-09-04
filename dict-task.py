# import datetime
# print(datetime.datetime.now().strftime("%x"))

pdt=[]
while True:
    print('''
1.Add Product
2.Update Product
3.Remove Product
4.View All Product
5.Search Product
6.Exit
      ''')
    ch=int(input("Enter Your Choice :"))
    if ch==1:
        name=input("Name Of Product :")
        qty=int(input("Quantity Of Product :"))
        cost=int(input("Cost Of Product :"))
        pay=input("Modes Of Payment :")
        date=int(input("Date Of Purchase :"))
        pdt.append({'name':name,'qty':qty,'cost':cost,'pay':pay,'date':date})
    elif ch==2:
        name=input("Name Of Product :") 
        f=0
        for i in pdt:
            if i['name']==name:
                f=1
                while True:
                    print('''
1.Quantity
2.Cost
3.Date Of Purchase
4.Mode Of payment
5.Exit                                                                             
''') 
                    sub_ch=int(input("Enter Your Choice For Updation :"))
                    if sub_ch==1:
                        new_qty=int(input("Enter New Quantity :"))
                        i['qty']=new_qty
                    elif sub_ch==2:
                        new_cost=int(input("Enter New Cost :"))
                        i['cost']=new_cost 
                    elif sub_ch==3:
                        date=int(input("Date Of Purchase :"))
                    elif sub_ch==4:
                            
                    elif sub_ch==5:
                        break         
        if f==0:
            print('Product Name Not Found')    
    elif ch==3:
        name=input("Enter Name Of The Product :")
        f==0
        for i in pdt:
            if i['name']==name:
                pdt.remove(i) 
                f=1
        if f==0:
            print("Product Name Not Found")                     
    elif ch==4:
        print('{:<10} {:<5}{:<10}'.format('name','qty','cost','date'))  
        print('_'*30)
        for i in pdt:
             print('{:<10} {:<5}{:<10}'.format(i['name'],i['qty'],i['cost'],i['date']))
    elif ch==5:
        name=input("Name Of Product :")
        f=0
        for i in pdt:
            if i['name']==name:
                print(i)
                f=1
        if f==0:
            print("Product Name Not Found")  
    elif ch==6:
        break
    else:
        print("Invalid Choice")



