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
#     # print(i ,'*', a ,'=',i*a)
#     f.write(str(i)+'*'+str(a)+'='+str(i*a)+'\n')

f=open('Python/demo1.txt','w')
a=int(input("Enter a no :"))

for i in range(1,6):
    # print(i ,'*', a ,'=',i*a)
    f.write(str(i)+'*'+str(a)+'='+str(i*a)+'\n')
