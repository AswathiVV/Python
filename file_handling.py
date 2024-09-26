# f=open('Python/demo.txt','x')
# f.write('welcome \n hello \n hi')

# f=open('Python/demo.txt','r')
# a=f.read()
# print(a)
'''Welcome'''
# or
# print(f.read())
'''Welcome'''




# f=open('Python/demo.txt','r')
# a=f.read(5)

# f.seek(0)

# b=f.read()

# print(f.tell())
# print(a)
# print('_'*20)
# print(b)

'''
7
welco
____________________
welcome
'''

# f=open('Python/demo.txt','r')
# a=f.readline(5)
# b=f.readline()
# c=f.readline()
# print(a)
# print(b)
# print(c)
'''
welco
me 

hello 

'''

# f=open('Python/demo.txt','r')
# a=f.readline(5)
# b=f.readline()

# print(a)
# print(b)
# f.seek(0)
# l=f.readlines()
# print(l)

'''
welco
me 

['welcome \n', 'hello \n', 'hi']'''



# f=open('Python/demo.txt','r')
# l=f.readlines()
# f.seek(0)
# for i in range(len(l)):
#     a=f.readline().strip()
#     print(a)

'''
welcome
hello
hi
'''   

# f=open('Python/demo.txt','r')
# l=f.readlines()
# f.seek(0)

# for i in range(len(l)):
#     a=f.readline().strip()
#     rev=' '
#     rev=i+rev
    
# print(rev) 

'''
welcome 
hellowelcome 
hihellowelcome '''    

# f=open('Python/demo.txt','r')
# l=f.readlines()
# f.seek(0)
# for i in range(len(l)):
#     a=f.readline().strip()
#     print(a[::-1])   # slicing method

'''
emoclew
olleh
ih
'''

# f=open('Python/demo1.txt','w')
# f.write('\nWELCOME')

# f=open('Python/demo1.txt','a')
# f.write('\nWELCOME')
'''
WELCOME
WELCOME
WELCOME
'''




    #  print(x*y)







# f=open('Python/demo1.txt','w')
# a=int(input("Enter a no :"))

# for i in range(1,11):
#     print(i ,'*', a ,'=',i*a)
#     f.write(str(i)+'*'+str(a)+'='+str(i*a)+'\n')

'''
Enter a no :2
1 * 2 = 2
2 * 2 = 4
3 * 2 = 6
4 * 2 = 8
5 * 2 = 10
6 * 2 = 12
7 * 2 = 14
8 * 2 = 16
9 * 2 = 18
10 * 2 = 20
'''    


# task

# f=open('Python/demo1.txt','w')
# for i in range(1,11):
#     for a in range(1,6):
#          f.write(str(i)+'*'+str(a)+'='+str(i*a)+'\t')
#     f.write("\n")     
   
'''
1*1=1	1*2=2	1*3=3	1*4=4	1*5=5	
2*1=2	2*2=4	2*3=6	2*4=8	2*5=10	
3*1=3	3*2=6	3*3=9	3*4=12	3*5=15	
4*1=4	4*2=8	4*3=12	4*4=16	4*5=20	
5*1=5	5*2=10	5*3=15	5*4=20	5*5=25	
6*1=6	6*2=12	6*3=18	6*4=24	6*5=30	
7*1=7	7*2=14	7*3=21	7*4=28	7*5=35	
8*1=8	8*2=16	8*3=24	8*4=32	8*5=40	
9*1=9	9*2=18	9*3=27	9*4=36	9*5=45	
10*1=10	10*2=20	10*3=30	10*4=40	10*5=50	
'''   

# f=open('Python/demo1.txt','w')
# a=int(input("Enter a no :"))
# for i in range(1,11):
#     for j in range(1,a+1):
#          f.write(str(i)+'*'+str(j)+'='+str(i*j)+'\t')
#     f.write("\n")    
'''
Enter a no :6
1*1=1	1*2=2	1*3=3	1*4=4	1*5=5	1*6=6	
2*1=2	2*2=4	2*3=6	2*4=8	2*5=10	2*6=12	
3*1=3	3*2=6	3*3=9	3*4=12	3*5=15	3*6=18	
4*1=4	4*2=8	4*3=12	4*4=16	4*5=20	4*6=24	
5*1=5	5*2=10	5*3=15	5*4=20	5*5=25	5*6=30	
6*1=6	6*2=12	6*3=18	6*4=24	6*5=30	6*6=36	
7*1=7	7*2=14	7*3=21	7*4=28	7*5=35	7*6=42	
8*1=8	8*2=16	8*3=24	8*4=32	8*5=40	8*6=48	
9*1=9	9*2=18	9*3=27	9*4=36	9*5=45	9*6=54	
10*1=10	10*2=20	10*3=30	10*4=40	10*5=50	10*6=60	
 '''       

# f=open('Python/demo.txt','r')
# l=f.readlines()
# f.seek(0)
# letters=0
# for i in range(len(l)):
#     a=f.readline().strip()
#     for i in a:
#         if i !=' ':
#             letters+=1

# print(letters) 
'''
20
'''




# f=open('Python/demo.txt','r')
# l=f.readlines()
# f.seek(0)
# letters=0
# capital=0
# for i in range(len(l)):
#     a=f.readline().strip()
#     for i in a:
#         if i !=' ':
#             if i.isupper():
#                 capital+=1
#             letters+=1

# print(letters)   
# print('Capital :',capital)
# print('Small :',letters-capital)  
'''
20
Capital : 3
Small : 17
'''

# f=open('Python/demo.txt','r')
# l=f.readlines()
# f.seek(0)
# letters=0
# capital=0
# word=0
# for i in range(len(l)):
#     a=f.readline().strip()
#     s=a.split(' ')
#     for i in s:
#         if i !=' ':
#             word+=1

#     for i in a:
#         if i !=' ':
#             if i.isupper():
#                 capital+=1
#             letters+=1

# print("letters :",letters)   
# print('Capital :',capital)
# print('Small :',letters-capital)
# print("word :",word) 
# print("No of lines :",len(l))       


# f=open('Python/demo.txt','a')
# f.write('\nappend')

# import os

# os.remove('Python/demo2.txt')

# if os.path.exists('Python/demo2.txt'):
#     print('File Found')
# else:
#     print('File Not Found')    


# import os
# os.mkdir('sample')   # to create folder
   
# os.rmdir('sample')    # to delete folder
      


# contains error

# print("WELCOME")
# a='welcome'
# b=20
# try:
#     print(a+b)
# except:
#     print("an error")
# else:
#     print("else")
# finally:
#     print("pgm ends")
# print("SAMPLE PRINT")                

'''
WELCOME
an error
pgm ends
SAMPLE PRINT
'''   



# no error

# print("WELCOME")
# a='welcome'
# b='20'
# try:
#     print(a+b)
# except:
#     print("an error")
# else:
#     print("else")
# finally:
#     print("pgm ends")
# print("SAMPLE PRINT") 

'''
WELCOME
welcome20
else 
pgm ends
SAMPLE PRINT
'''



# l=[1,2,3,4,5,'a',6,7,8]
# sum=0
# for i in l:
#        try:
#          sum+=i
#        except:
#             # print('error') 
#              pass
# print('sum:',sum) 

'''36'''

l=[1,2,3,4,5,'a',6,7,8]
sum=0
for i in l:
         if type(i)==int or type(i)==float:
            sum+=i
print('sum:',sum) 

'''sum: 36'''
    
    
