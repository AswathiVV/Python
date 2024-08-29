# l=[10,11,10,'abc',5.8]
# # for i in l:
# if 10 in l:
#     print("Available")
# else:
#     print('Not Available') 
            
# l=[10,11,10,'abc',5.8]
# print(l[0])
# print(l[3])

'''[10, 11, 10, 'manu', 5.8]'''
# l=[10,11,10,'abc',5.8]
# l[3]='manu'
# print(l)

'''[10, 11, 12, 'abc', 5.8]'''
# l[2]=12
# print(l)

# 1.Appand

'''[10, 'python', [1, 2, 3]]'''
# l=[]
# l.append(10)
# l.append('python')
# l.append([1,2,3])
# print(l)



# 2.Extend

'''['a', 'b', 'c']'''
# l=[]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
# l.extend(['a','b','c'])
# print(l)

# 3.Insert

'''['HI']'''
# l=[]
# l.insert(0,'HI')
# print(l)

'''['HI', 1, 2, 3]'''
# l=[1,2,3]
# l.insert(0,'HI')
# print(l)


# 1.Clear

'''[]'''
# l=[1,2,3]
# l.clear()
# print(l)

# 2.pop

'''[10, 'abc', 25]'''
# l=[10,'abc',25,11]
# l.pop()
# print(l)

'''[10, 'abc', 11]'''
# l=[10,'abc',25,11]
# l.pop(2)
# print(l)


#3.Remove

'''[10, 25, 11]'''
# l=[10,'abc',25,11]
# l.remove('abc')
# print(l)



'''[2, 4, 5, 6, 10, 11]'''

# l=[10,11,6,2,4,5]
# l.sort()
# print(l)

'''[5, 4, 2, 6, 11, 10]'''

# l=[10,11,6,2,4,5]
# l.reverse()
# print(l)

'''140718359895680
   140718359895680
   l= [10, 11, 6, 2, 4, 5]
   l1= [10, 11, 6, 2, 4, 5]
   l= [10, 11, 6, 2, 4, 5]
   l1= [10, 11, 6, 2, 4, 5]'''

# l=[10,11,6,2,4,5]
# l1=l
# print(id(l))
# print(id(l1))
# print("l=",l)
# print('l1=',l1)
# l1.pop
# print("l=",l)
# print('l1=',l1)


'''140692757126784
   140692757204160
   l= [10, 11, 6, 2, 4, 5]
   l1= [10, 11, 6, 2, 4, 5]
   l= [10, 11, 6, 2, 4, 5]
   l1= [10, 11, 6, 2, 4, 5]'''

# l=[10,11,6,2,4,5]
# l1=l.copy()
# print(id(l))
# print(id(l1))
# print("l=",l)
# print('l1=',l1)
# l1.pop
# print("l=",l)
# print('l1=',l1)

'''2'''
# l=[10,11,6,2,4,5]
# print(l.index(6))


'''Odd numbers: [1, 3, 5, 7]
   Even numbers: [2, 4, 6, 8]'''

# l=[1,2,3,4,5,6,7,8]
# sum=0

# for i in l:
#     if i % 2 == 0:
        
#        sum+=i
#     print(i)
        

# print(sum)


'''Sum : 36'''
# l = [1, 2, 3, 4, 5, 6, 7, 8]
# sum = 0
# for i in l:
#        sum += i
# print("Sum :",sum)


'''emoclew
   nohtyp
   olleh'''

# l=['welcome','python','hello']
# for i in l:
#     print(i[::-1])


'''Sum : 18.8'''

# l=[1,10,5.8,'abc',2]     
# sum = 0
# for i in l:
#        if type(i)==(int) or type(i)==float:
#         sum += i
# print("Sum :",sum)


'''[5,8,1,2,3]'''

# l=[5,8,5,1,2,3,8,5]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)   
# 

'''Enter limit : 5
Enter Name :A
Enter Name :B
Enter Name :C
Enter Name :D
Enter Name :E
['A', 'B', 'C', 'D', 'E']'''
# names=[]
# limit=int(input('Enter limit : '))     
# for i in range(limit):
#     name=input("Enter Name :")
#     names.append(name)
# print(names)    


'''Enter limit : 2
   Enter Name :Ammu
   Enter Age :21
   Enter Mark :50
   Enter Name :Aswathi
   Enter Age :23
   Enter Mark :49
   [['Ammu', 21, 50], ['Aswathi', 23, 49]]'''

# std=[]
# limit=int(input('Enter limit : '))     
# for i in range(limit):
#     name=input("Enter Name :")
#     age= int(input("Enter Age :"))
#     mark=int(input("Enter Mark :"))
#     std.append([name,age,mark])
# print(std)  


'''
1.Add STD
2.View STD
3.Update STD
4.Delete STD
      
Enter Your Choice :1
Enter Name :Aswathi
Enter Age :20
Enter Mark :70

1.Add STD
2.View STD
3.Update STD
4.Delete STD
      
Enter Your Choice :2
name      age  mark 
____________________
Aswathi   20   70   
  

1.Add STD
2.View STD
3.Update STD
4.Delete STD
      
Enter Your Choice :3

1.Add STD
2.View STD
3.Update STD
4.Delete STD
      
Enter Your Choice :4

1.Add STD
2.View STD
3.Update STD
4.Delete STD
      
Enter Your Choice : '''

# std=[]
# while True:
#     print('''
# 1.Add STD
# 2.View STD
# 3.Update STD
# 4.Delete STD
#       ''')
#     choice=int(input("Enter Your Choice :"))
#     if choice==1:
#         name=input("Enter Name :")
#         age= int(input("Enter Age :"))
#         mark=int(input("Enter Mark :"))
#         std.append([name,age,mark])
#     elif choice==2:
#         print('{:<10}{:<5}{:<5}'.format('name','age','mark'))  
#         print('_'*20)  
#         for i in std:
#              print('{:<10}{:<5}{:<5}'.format(i[0],i[1],i[2]))
            
        