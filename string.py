# a='python'
# print('\tpython\n','\tjava')

# print(a[0])
# print(a[-1])
# print(a[-6])
# print(a[5])

# a='''python
# php'''
# print(a)

# a="""python
# php"""
# print(a)

# a="python"
# print(a[0:5])
# print(a[5])
# print(a[:5])
# print(a[-6:])
# print(a[-3:])
# print(a[0:6])
# print(a[-6:0])
# print(a[3:6])
# print(a[0:-1])

# a="python"
# print(a[::-1])
# a="ASWATHI"
# print(a[::-1])
# print(a[::-4])

# a=input("enter a string")
# print(a)
# print(a[::-1])
# print(a==a[::-1])

# a="welcome to All"
# a=a.capitalize() 
# print(a.capitalize())

# print(a.upper())
# print(a.lower())

# b="ADEF"
# print(b.isupper())
# b="adef"
# print(b.islower())

# a="python"
# print(a.center(40))

# print(a.count('p'))
# print(a.count('m'))

# print(a.endswith('g'))
# print(a.endswith('n'))

# print(a.startswith('p'))
# print(a.find('e'))
# a="         py           "
# print(a.strip())
# print(a.lstrip())
# print(a.rstrip())

print("{:<16}{:<8}{:<8}".format("Name",'Age','Mark'))
print("{:<16}{:<8}{:<8}".format("a",'22','40'))
print("{:<16}{:<8}{:<8}".format("b",'20','39'))
item=input("enter an item")
price=int(input("enter price"))
print(f"its an {item}, its price {price} rs")