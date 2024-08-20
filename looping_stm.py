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

a=input('str:')
l=len(a)
i=0
rev=''
while i<l:
    rev=a[i]+rev
    i+=1
print(rev)


