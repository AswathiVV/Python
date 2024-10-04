# import re           # re=regular expression
# a='abcd'
# print(re.search('a',a))
'''
<re.Match object; span=(0, 1), match='a'>
'''

# print(re.search('abcd',a))
'''
<re.Match object; span=(0, 4), match='abcd'>
'''

# a='abcd'
# print(re.search('s',a))
'''
None
'''
# a='abcd'
# if re.search('s',a):
#     print('match')
# else:
#     print('not match')    
'''
not match
'''    

# a='abcd'
# if re.search('a',a):
#     print('match')
# else:
#     print('not match')
'''
match
'''    


# a='abcd'
# print(re.search('a',a))
'''<re.Match object; span=(0, 1), match='a'>'''

# print(re.search('a.',a))
'''<re.Match object; span=(0, 2), match='ab'>'''

# print(re.search('b.',a))
'''<re.Match object; span=(1, 3), match='bc'>'''

# print(re.search('c.',a))
'''<re.Match object; span=(2, 4), match='cd'>'''

# print(re.search('d.',a))
'''None'''

# print(re.search('b..',a))
'''<re.Match object; span=(1, 4), match='bcd'>'''



# print(re.search('a.*',a))
'''<re.Match object; span=(0, 4), match='abcd'>'''

# print(re.search('b.*',a))
'''<re.Match object; span=(1, 4), match='bcd'>'''

# print(re.search('c.*',a))
'''<re.Match object; span=(2, 4), match='cd'>'''

# print(re.search('d.*',a))
'''<re.Match object; span=(3, 4), match='d'>'''


# print(re.search('a.+',a))
'''<re.Match object; span=(0, 4), match='abcd'>'''

# print(re.search('b.+',a))
'''<re.Match object; span=(1, 4), match='bcd'>'''

# print(re.search('c.+',a))
'''<re.Match object; span=(2, 4), match='cd'>'''

# print(re.search('d.+',a))
'''None'''


# print(re.search('a.?',a))
'''<re.Match object; span=(0, 2), match='ab'>'''

# print(re.search('b.?',a))
'''<re.Match object; span=(1, 3), match='bc'>'''

# print(re.search('c.?',a))
'''<re.Match object; span=(2, 4), match='cd'>'''

# print(re.search('d.?',a))
'''<re.Match object; span=(3, 4), match='d'>'''



# print(re.search('abcd',a))
'''<re.Match object; span=(0, 4), match='abcd'>'''

# print(re.search('[abcd]',a))
'''<re.Match object; span=(0, 1), match='a'>'''


# a='abcd'
# print(re.search('[a-z]',a))
'''<re.Match object; span=(0, 1), match='a'>'''

# a='ABCD'
# print(re.search('[A-Z]',a))
'''<re.Match object; span=(0, 1), match='A'>'''

# print(re.search('[A-z]',a))
'''<re.Match object; span=(0, 1), match='A'>'''


# a='ABCD'
# print(re.search('[a-z]',a))
'''None'''

# a='1234'
# print(re.search('[0-9]',a))
'''<re.Match object; span=(0, 1), match='1'>'''

# print(re.search('[6-9]',a))
'''None'''


# a='abc123'
# print(re.search('[a-z][0-9]',a))
'''<re.Match object; span=(2, 4), match='c1'>'''

# a='123'
# print(re.search('[a-z0-9]',a))
'''<re.Match object; span=(0, 1), match='1'>'''

# a='abcd'
# print(re.search('[a-z0-9]',a))
'''<re.Match object; span=(0, 1), match='a'>'''

# a='abc123'
# print(re.search('[a-z0-9]',a))
'''<re.Match object; span=(0, 1), match='a'>'''

# a='abc123'
# print(re.search('[a-z].*[0-9]',a))
'''<re.Match object; span=(0, 6), match='abc123'>'''

a='abc1'
# print(re.search('[a-z].*[0-9]',a))
'''<re.Match object; span=(0, 4), match='abc1'>'''

# print(re.search('[a-z].+[0-9]',a))

# print(re.search('[a-z].?[0-9]',a))

# print(re.search('[a-z].?[0-9].+',a))
# print(re.search('[a-z].?[0-9].?',a))




# import re
# a='0123456789'
# if len(a)==10 and re.search('[6-9].{9}',a) and a.isdigit():
#     print("valid")
# else:
#     print("invalid")  
'''
invalid
'''     
# import re
# a='6123456789'
# if len(a)==10 and re.search('[6-9].{9}',a) and a.isdigit():
#     print("valid")
# else:
#     print("invalid")  
'''valid'''    

# import re
# a='612345678x'
# if len(a)==10 and re.search('[6-9].{9}',a) and a.isdigit():
#     print("valid")
# else:
#     print("invalid")  
'''invalid'''    

import re
a='a@gmail.com'
print(re.search('^[a-z].*@gamil.com$',a))
'''
None
'''

    