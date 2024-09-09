# t=(1,2,3,'abc',5.8)
# T=()
# for i in t:
#     print(i)

# if 2 in t:
#     print('True')
# else:
#     print('False')

# print(t[0])
# print(t[2])

# t=(1,2,[10,11])
# # print (t[2])
# t[2].append(12)
# print(t)
# '''(1, 2, [10, 11, 12])'''

# t=(1,2,3,4)
# print(t.index(2))
# print(t.count(2))

# t=(1,2,3,4)
# l=list(t)
# print(l)
# '''[1, 2, 3, 4]'''

# t=(1,2,3,4)
# l=list(t)
# l.pop()
# print(l)

# t=(1,2,3,4)
# l=list(t)
# t=tuple(l)
# print(l)

# d={'name':'anu','age':20}
# l=list(d)
# print(l)
'''['name', 'age'] '''

# s=set()
# s1={1,2,3,4,'abc',5.8,1,2}
# print(s1)

# l=[1,2,3,1,2,3]
# s=set(l)
# l=list(s)
# print(l)

# add

# s={1,2,3}
# s.add(10)    
# print(s)
'''{10, 1, 2, 3}'''

# difference

# s={10,1,2,3}
# print(s.difference({10,1,5,6}))
'''{2, 3}'''

# s={10,1,2,3}
# s1={10,1,5,6}
# print(s.difference(s1))
'''{2, 3}'''

# discard

# s={1,2,3}
# s.discard(1)
# print(s)
'''{2, 3}'''

# s={1,2,3}
# s.remove(2)
# print(s)
'''{1, 3}'''

# pop



# intersection

# s={1,2,3,4,5}
# s1={1,2,3,6,8}
# print(s.intersection(s1))

'''{1, 2, 3}'''

# union

# s={1,2,3,4,5}
# s1={1,2,3,6,8}
# print(s.union(s1))

'''{1, 2, 3, 4, 5, 6, 8}'''

# isdisjoint

# s={1,2,3,4,5}
# s1={1,2,3,6,8}
# print(s.isdisjoint(s1))
'''False'''

# s={1,2,3,4,5}
# s2={10,11,12}
# print(s.isdisjoint(s2))
'''True'''

# issubset

# s={1,2,3,4,5}
# s1={1,2,3,6,8}
# print(s.issubset(s1))
'''False'''

# issuperset

# s={1,2,3,4,5}
# s1={1,2,3,6,8}
# print(s.issuperset(s1))
'''False'''

# s={1,2,3,4,5}
# s2={10,11,12}
# print(s.issuperset(s2))
'''False'''

# symmetric difference


# s={1,2,3,4,5}
# s1={1,2,3,6,8}
# print(s.symmetric_difference(s1))
'''{4, 5, 6, 8}'''

# difference update

# s={1,2,3,4,5}
# s1={1,2,3,6,7}
# s.difference_update(s1)
# print(s)
# print(s1)
'''{4, 5}
{1, 2, 3, 6, 7}'''

# intersection update

# s={1,2,3,4,5}
# s1={1,2,3,6,7}
# s.intersection_update(s1)
# print(s)
# print(s1)
'''{1, 2, 3}
{1, 2, 3, 6, 7}'''

# symmetric difference update
# s={1,2,3,4,5}
# s1={1,2,3,6,7}
# s.symmetric_difference_update(s1)
# print(s)
# print(s1)
'''{4, 5, 6, 7}
{1, 2, 3, 6, 7}'''


# php=set()
# e=int(input("Enter a no :"))
# for i in range(e):
#     s=input("Enter Name ")
#     php.add(s)
# print("php =",php)

# python=set()
# e=int(input("Enter a no :"))
# for i in range(e):
#     s=input("Enter Name ")
#     python.add(s)
# print("python =",python)

# java=set()
# e=int(input("Enter a no :"))
# for i in range(e):
#     s=input("Enter Name ")
#     java.add(s)
# print("java =",java)

# data=php.intersection(python)
# data1=java.intersection(data)
# print(data1)

# data=python.difference(php)
# data1=python.difference(java)
# print(data1)


















