      # filter


# l=[1,2,3,4,5,6,7,8]
# for i in l:
#     if i % 2 == 0:
#      print(i)

# l=[1,2,3,4,5,6,7,8]
# print(list(filter(lambda x:x%2==0,l)))
'''[2, 4, 6, 8]'''

# l=[1,2,3,4,5,6,7,8]
# print(list(filter(lambda x:x%2==1,l)))
'''[1, 3, 5, 7]'''

# l=[1,2,3,4,5,6,7,8]
# def num(x):
#     return x%2==0
# print(list(filter(num,l)))
'''[2, 4, 6, 8]'''

# l=[1,2,3,4,5,6,7,8]
# def num(x):
#     return x%2==1
# print(list(filter(num,l)))
'''[1, 3, 5, 7]'''


# l=['apple','orange','kiwi']
# print(list(filter(lambda x:'a' in x,l)))
'''['apple', 'orange']'''


# l=['apple','orange','kiwi']
# def fun(x):
#     return 'a' in x
# print(list(filter(fun,l)))
'''['apple', 'orange']'''


     # map

# l=[1,2,3,4,5,6,7,8]
# print(list(map (lambda x:x**3,l)))

'''[1, 8, 27, 64, 125, 216, 343, 512]'''  


# l=[1,2,3,4,5,6,7,8]
# def fun(x):
#     return x**3
# print(list(map(fun,l)))
'''[1, 8, 27, 64, 125, 216, 343, 512]'''  