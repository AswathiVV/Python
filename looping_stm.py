# i=int(input("Enter Starting Value :"))
# e=int(input("Enter Ending Value :"))
# while i<=e:
#     print(i)
#     i+=1

# i=int(input("Enter Starting Value :"))
# e=int(input("Enter Ending Value :"))
# while i<=e:
#     print(i)
#     i+=5

# i=int(input("Enter Starting Value :"))
# e=int(input("Enter Ending Value :"))
# while i<=e:
#     print(i)
#     i+=10

# i=1
# e=int(input("Enter limit :"))
# while i<=e:
#     print("python")
#     i+=1

# i=int(input("Enter Starting Value :"))
# e=int(input("Enter Ending Value :"))
# sum=0
# while i<=e:
#     sum=sum+i
#     i+=1
# print('sum:',sum)    

# i=int(input("Enter Starting Value :"))
# e=int(input("Enter Ending Value :"))
# while i<=e:
#     if i%2==0:
#         print(i) 
#     i+=1

# i=int(input("Enter Starting Value :"))
# e=int(input("Enter Ending Value :"))
# sum=0
# while i<=e:
#     if i%3==0:
#         sum=+i
#     i+=1
# print('sum: ',sum) 


# i=int(input("Enter Starting Value :"))
# e=int(input("Enter Ending Value :"))
# sum=0
# while i<=e:
#     if i%2==0:
#         sum+=i
#     i+=1
# print('sum: ',sum) 

# i=int(input("Enter Starting Value :"))
# e=int(input("Enter Ending Value :"))
# sum=0
# while i<=e:
#     if i%2!=0:
#         sum+=i
#     i+=1
# print('sum: ',sum) 


# x=int(input("Enter Starting Value :"))
# y=int(input("Enter Ending Value :"))
# i=1
# sum=0
# e=int(input("Enter a no. :"))
# while i<=10 and x<=y:
#     print(i,'*',e,'=',i*e and 'sum: ',sum)
#     i+=1
#     x+=1


# i=int(input("Enter Starting Value :"))
# e=int(input("Enter Ending Value :" ))
# sum=0
# odd_sum=0
# normal_sum=0
# while i<=e:
#     normal_sum+=i
#     if i%2==0:
#         sum+=i
#     else:
#         odd_sum+=1
#     i+=1
# print('sum: ',sum) 
# print('odd_sum: ',odd_sum)
# print('normal_sum: ',normal_sum)


# i=1
# e=int(input("Enter Ending Value :"))
# Factorial=1
# while i<=e:
#     Factorial*=i
#     i+=1
# print('Factorial_sum:',Factorial)


# a=int(input("Enter a no. :"))
# while a>0:
#     d=a%10
#     print(d)
#     a//=10

# a=int(input("Enter a no. :"))
# rev=0
# while a>0:
#     d=a%10
#     rev=rev*10+d
#     a//=10
# print(rev)

# a=int(input("Enter a no. :"))
# rev=0
# while a>0:
#     d=a%10
#     rev=rev+d
#     a//=10
# print(rev)


     
# a=input('str:')
# l=len(a)
# i=0
# while i<l:
#     print(a[i])
#     i+=1

# a=input('str:')
# l=len(a)
# i=0
# rev=''
# while i<l:
#     rev=a[i]+rev
#     i+=1
# print(rev)

# for i in range (1,10):
#     print(i)
 
# for i in range(3,100,3):
#     print(i)

# for i in range(5):
#     print('welcome')

# start=int(input("Enter Starting Value:"))
# end=int(input("Enter Ending Value :"))
# sum=0
# for i in range(start,end+1):
#     sum+=i
# print(sum)    

# end=int(input("Enter a Value :"))
# rev=0
# for i in range (rev*10+(end%10)):
#         print(rev)


# i=int(input("Enter Starting Value :"))
# e=int(input("Enter Ending Value :" ))
# sum=0
# odd_sum=0
# normal_sum=0
# while i<=e:
#     normal_sum+=i
#     if i%2==0:
#         sum+=i
#     else:
#         odd_sum+=i
#     i+=1
# print('sum: ',sum) 
# print('odd_sum: ',odd_sum)
# print('normal_sum: ',normal_sum)
# a=int(input("Enter Starting Value :"))
# e=int(input("Enter Ending Value :" ))
# sum=0
# odd_sum=0
# normal_sum=0
# for i in range(a,e+1):
#     normal_sum+=i
#     if i%2==0:
#         sum+=i
#     else:
#         odd_sum+=i

# print('sum: ',sum) 
# print('odd_sum: ',odd_sum)
# print('normal_sum: ',normal_sum)


# e=int(input("Enter Ending Value :"))
# factorial=1
# for i in range(1,e+1):
#     factorial*=i
# print('factorial_sum',factorial)    

# e=int(input("Enter a Value :"))

# for i in range(1,11):
#     print(i,'*',e,'=',i*e)


# a=input("Enter a string :")
# rev=''
# for i in a:
#     rev=i+rev
# print(rev)    


# a=input("Enter a string :")
# for i in a:
#     print(i)  


# for i in range(4):
#     print('i=',i)
#     for j in range(3):
#         print('/t j=',j)

# for i in range(5):
#     for j in range(5):
#         print(j,end="\t")
#     print()    

# for i in range(5):
#     a=10
#     for j in range(4):
#         print(a,end="\t")
#         a+=1
#     print()    

# for i in range(3):
#     for j in range(1):
#      print(i,end="") 
#     print(i+1,end="")  
#     print(i+2,end="")  

#     print()     

# for i in range(3):
#     for j in range(3):
#      print(i,end="\t") 
#      i+=1
     
     

#     print()  

# a=0
# for i in range(3):
#     for i in range(3):
#         print(a,end="")
#         a+=1
#     print()    

# a=0



# for i in range(4):
#     if i%2==0:
#         for j in range(3):
#             print(j,end="")
#     else:
#         for j in range(3):
#             print(2-j,end="")
#     print() 

'''0 1 2
   2 1 0
   0 1 2
   2 1 0'''        
        
   
'''0 1 4
   0 1 4
   9 16 25
   9 16 25'''





# for i in range(4):
#    for j in range(3):
#     if i < 2:
#         value = [0, 1, 4]
#         print(i, end=' ')
#     else:
#         value = [9, 16, 25]
#         print(i, end=' ')
#     print() 
# Loop through the number of rows
# for i in range(4):
    
#     if i < 2:
#         a= 0 if i == 0 else 1
#     else:
#         a=9
    
#     for j in range(3):
        
#         print(a + j * j, end=' ')
#     print()


# for i in range(4):
    
   #  if i < 2:
   #      base = 0
   #      increments = [0, 1, 4]
   #  else:
   #      base = 9
   #      increments = [0, 1, 4]

    
   #  for j in range(3):
   #      print(base + increments[j] ** 2, end=' ')
    
    
   #  print()

# for i in range(4):
#     for j in range(3):
#          if i < 2:
#           a= 0
#          print(a+ j * j, end=' ')
#     else:
#         a= 9
#     print()


'''1 3 5
   7 9 11
   13 15 17'''
# a=1
# for i in range(3):
#     for i in range(3):
#         print(a,end="\t")
#         a+=2
#     print()  
# 


'''A B C
   A B C
   A B C
   
   65 66 67
   65 66 67
   65 66 67''' 

# for i in range(3):
#     a=65
#     for j in range(3):
#         print(chr(a+j),end="")
#     print()    

'''1
   2 3
   4 5 6
   7 8 9 10'''

# start=1
# for i in range(1,5): 
#     for j in range(i):
#         print(start, end=' ')
#         start+= 1
#     print()

'''1
   2 1
   3 2 1
   4 3 2 1'''

# for i in range(1,5):
#     for j in range(i):
#         print(i-j,end=" ")
#     print()    


'''5 # #
   # 5 #
   # # 5'''

# for i in range(3):
#     for j in range(3):
#         if i==j:
#             print('5', end=' ')
#         else:
#             print('#', end=' ')
    
#     print()

'''A
   A B
   A B C'''

# for i in range(1,4):
#    a=65
#    for j in range(i):
#        print(chr(a+j),end="\t")
#    print()    
 
'''A 
   B A
   C B A'''
       
# a=64
# for i in range(1,4):
#     for j in range(i):
#         print(chr((a+i)-j),end=" ")
      
#     print()   
    

'''A
   B B
   C C C''' 

# method-1

# a=65
# for i in range(1,4):
#    for j in range(i):
#        print(chr(a),end="") 
#    print()
#    a+=1

# Method-2

# a=64
# for i in range(1,4):
#    for j in range(i):
#        print(chr(a+i),end="") 
#    print()
   
'''0 1 2
   A B C
   0 1 2
   A B C'''
# a=65
# for i in range(4):
#     if i%2==0:
#         for j in range(3):
#             print(j,end=" ")
#     else:
#         for j in range(3):
#             print(chr(a+j),end=" ")
#     print() 

'''  * *
     * * * *
     *
     * * *    '''
# l=[2,4,1,3]
# for i in l:
#     print('*'*i)
