# class syneefo:              # class
#     def python():
#         print("PYTHON")
#     def php():              # methods
#         print("PHP")

# std=syneefo
# std.python()                # object
# std.php() 


# class Bank():
#     def __init__(s):
#         s.bal=0
#     def deposit(self,amt):
#         self.bal+=amt
#         print("Amount Added :",self.bal)
#     def withdraw(self,amt):
#         self.bal-=amt
#         print("Withdraw :",self.bal)
#     def display(self):
#         print('display :',self.bal)        
# user1=Bank()
# user1.deposit(1000)                
# user1.withdraw(500)
# user1.display()
'''
Amount Added : 1000
Withdraw : 500
display : 500
'''
# user2=Bank(500)
# print(user2.bal)

# class Demo():
#     def __init__(self,a):
#         print(a)
# obj=Demo(12)  

'''12'''      

# class company():
#     def __init__(s):
#         s.bal=0
#     def profit(self,amt):
#         self.bal+=amt
#         print("profit :",self.bal)
#     def loss(self,amt):
#         self.bal-=amt
#         print("loss :",self.bal)
#     def display(self):
#         print('display :',self.bal) 

# act=company()
# act.profit(100000)
# act.loss(20000)
# act.display()


# class Demo():
#     def __init__(self,a):
#         print(a)
#     def a(self,name,age):
#         print('name',name)
#         # print('age',age)
# dtls=Demo
# dtls(age=20,name='a')        

# obj=Demo(12)  




# single inheritance


# class parent:
#     def shop(self):
#         print("shop")
#     def car(self):
#         print("car")
# class child(parent):
#     def bike(self):
#         print("bike")

# manu=child()
# manu.bike()
# manu.car()
# manu.shop()


# class synnefo:
#     def php(self):
#         print("php")
#     def python(self):
#         print("python")

# class novavi(synnefo):
#     def web_dev(self):
#         print("web development")  
#     def dm(self):
#         print("dm works")

# manu=novavi()
# manu.python()
# manu.php()
# manu.web_dev()
                    
# std1=synnefo()
# std1.php()  



# multiple inheritance


# class mom:
#     def shares(self):
#         print("shares")
#     def land(self):
#         print("land") 
# class dad:
#     def investments(self):
#         print("investments")
#     def assets(self):
#         print("assets")
# class child(mom,dad):
#     def bike(self):
#         print("bike")

# riya=child()
# riya.assets()
# riya.shares()
# riya.bike()


# class school:
#     def reports(self):
#         print('reports')
#     def lab(self):
#         print('lab')
# class library:
#     def books(self):
#         print('books')
#     def lib_room(self):
#         print('library room') 
# class std1(school,library):
#     def id_card(self):
#         print('id card')                       

# sana=std1()
# sana.lab()
# sana.books()
# sana.id_card()



# multilevel inheritance


# class grand_father:
#     def shares(self):
#         print("shares")
#     def land(self):
#         print("land") 

# class father(grand_father):
#     def investments(self):
#         print("investments")
#     def assets(self):
#         print("assets")

# class child(father):
#     def bike(self):
#         print("bike")

# anu=child()
# anu.shares()
# anu.assets()
# anu.bike()

# manu=father()
# manu.land()
# manu.investments()


# class dep:
#     def employees(self):
#         print('employee details')
#     def works(self):  
#         print('work details')   
# class dep_managers(dep):
#     def reports(self):
#         print('reports')
# class dep_of_mgt(dep_managers):
#     def final_reports(self):
#         print('final reports')    

# mg=dep_of_mgt()
# mg.employees()
# mg.reports()
# mg.final_reports()     


# higherarcial inheritance

# class mom:
#      def shares(self):
#         print("shares")
#      def assets(self):
#         print("assets")

# class child1(mom):
#     def car(self):
#         print('car')     

# class child2(mom):
#     def bike(self):
#         print('bike')

# manu=child1()
# manu.assets()
# manu.shares()
# manu.car()   

# anu=child2()
# anu.assets()
# anu.shares()
# anu.bike()


class BOD:
    def final_reports(self):
        print('final reports')
    def plans_and_policies(self):
        print('plans & policies')
class production_dep(BOD):
    def employees(self):
        print('emp')    
class sales_dep(BOD) :
    def employees(self):
        print('emp') 


p=production_dep()
p.final_reports()

s=sales_dep()
p.final_reports

   
