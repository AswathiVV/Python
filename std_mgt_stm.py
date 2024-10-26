std=[]
while True:
    print('''
1.ADD STUDENT
2.VIEW STUDENT
3.UPDATE STUDENT
4.DELETE STUDENT
5.SEARCH
6.EXIT
          ''')
    choice=int(input("ENTER YOUR CHOICE :"))
    if choice==1:
        name=int(input("ENTER MARK :"))
        age=int(input("Enter Age :"))
        mark=int(input("Enter Mark :"))
        std.append({'name':name,'age':age,'mark':mark})