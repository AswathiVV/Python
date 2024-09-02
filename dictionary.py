# d={'name':'anu','age':20,'mark':20}
# print(d['name'])
# d['name']='Aswathi'
# print(d)
# d['place']='EKM'
# print(d)

# for i in d:
#     print(i,d[i])
'''name anu
   age 20
   mark 20'''

# for i in d:
#     print(i)
'''name
   age
   mark'''

# for i in d:
#     print (d[i])
'''anu
   20
   20'''

# if d['name']=='anu':
#     print('True')
# else:
#     print('False')  
# '''True'''  

# print(d.get ('name'))
'''anu'''  

# d.update({'name':'Akhil'})
# print(d)
'''{'name': 'Akhil', 'age': 20, 'mark': 20}'''

# d.pop('name')
# print(d)
'''{'age': 20, 'mark': 20}'''

# d.popitem()
# print(d)
'''{'name': 'anu', 'age': 20}''' 

# print(d.get('place'))
'''None'''

# d={}
# l=['name','age','place','mark']
# d=d.fromkeys(l)
# print(d)
'''{'name': None, 'age': None, 'place': None, 'mark': None}'''

# d={}
# d.setdefault('name')
# print(d)
'''{'name': None}'''





std=[]
while True:
    print('''
1.Add STD
2.View STD
3.Update STD
4.Delete STD
5.Search
6.Exit
      ''')
    choice=int(input("Enter Your Choice :"))
    if choice==1:
        name=input("Enter Name :")
        age=int(input("Enter Age :"))
        mark=int(input("Enter Mark :"))
        std.append({'name':name,'age':age,'mark':mark})
    elif choice==2:
        print('{:<10}{:<5}{:<5}'.format('name','age','mark'))  
        print('_'*20)  
        for i in std:
             print('{:<10}{:<5}{:<5}'.format(i['name'],i['age'],i['mark']))
    elif choice==3:
        name=input("Enter Name :")
        f=0
        for i in std:
           if i['name']==name:
              mark=int(input("Enter Your Mark :"))
              i['mark']=mark
              f=1
        if f==0:
            print('Name Not found')  
    elif choice==4:
        name=input("Enter Name :")
        f=0
        for i in std:
            if i['name']==name:
                std.remove(i)
                f=1
        if f==0:
              print('Name Not Fount')
    elif choice==5:
        name=input("enter Name :")  
        f=0
        for i in std:
            if i['name']==name:
                print(i)
                f=1
        if f==0:
            print("Name Not Found") 
    elif choice==6:
        break
    else:
        print("Invalid Choice")                        


      

                      
                
                 
            
            
            
