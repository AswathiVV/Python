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
# l = [1, 2, 3, 4, 5, 6, 7, 8]

# odd = []
# even= []

# for i in l:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# print("Odd numbers:", odd)
# print("Even numbers:", even)

'''Sum : 36'''
# l = [1, 2, 3, 4, 5, 6, 7, 8]
# sum = 0
# for i in l:
#        sum += i
# print("Sum :",sum)

  