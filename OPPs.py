# ✅ Abstraction, Encapsulation, Inheritance and Polymorphism is for mejor things for Oops.

# 6                   # 🟢 Abstraction

#Hiding the inplemntion details of a class and only share necassary faetures to the user.

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("Car started...")

# c_1 = Car()
# c_1.start()


# 7                   # 🟢 Encapsulation

# wrapping data and func into a single unit (obj).
# abhi taak jo humne jo kra hai vo Abstraction and Encapsulation kiya hai.
 
# class student:
#     Course = "BCA"
#     Branch = "CSE"
#     def __init__(self, fullName, marks): # parameter(self) iss compulsery.
#         self.name = fullName
#         self.marks = marks
#         print("adding new student in Dataabase...");

# s1 = student("Juned Khan", 97);
# print(s1.name, )
# print(s1.Course)
# print(s1.Branch)

# s2 = student("Zuned Khan", 99);
# print(s1.name, s2.marks)
# print(s1.Course)
# print(s1.Branch)


# 8                   # 🟢 del keyword

# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Zuned")
# print(s1.name)
# del s1.name
# print(s1.name)


# # 7                   # 🟢 private

# class Account:
#     def __init__(self, balance, account_password):
#         self.balance = balance
#         self.__account_pass = account_password

#     # debit method
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited")

#     # credits method
#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "was Credited")

#     def __get_balance(self): # private
#         return self.balance
    
#     def reset_pass(self):
#         print(self.__account_pass)
    
# acc1 = Account("12345", "abcde")
# print(acc1.balance)
# # print(acc1.__account_pass) # this is not allowed
# print(acc1.reset_pass()) # this is allowed because class me likha hua hai



# # 9                   # 🟢 Inheritance

# class Car:
#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stoped...")

# class Toyota(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = Toyota("Fortuner")
# car1 = Toyota("Innova")

# print(car1.name)
# print(car1.start())
# print(car1.stop())


# 9                   # 🟢Types of Inheritance

# a. Single inh. 
# Upar wala example


# b. Multi-level inh.

# class Car:
#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stoped...")

# class Toyota(Car):
#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(Toyota):
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("Diesel")
# car1.start()


# c. Multiple inh.

class A:
    var_A = "Welcome to class A"
    
class B:
    var_B = "Welcome to class B"

class C(A, B):
    var_C = "Welcome to class B"

c1 = C();
print(c1.var_C)
print(c1.var_A)
print(c1.var_B)


# # qtn 2:
# class Account:
#     def __init__(self, balance, account_num):
#         self.balance = balance
#         self.account_num = account_num

#     # debit method
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited")

#     # credits method
#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "was Credited")

#     def get_balance(self):
#         return self.balance


# Account1 = Account(100000, 12345)
# Account1.debit(5000)
# Account1.credit(10000)
# Account1.get_balance()



#1                    # 🟢 Creating Class

# class student:
#     Course = "BCA"
#     Branch = "CSE"

#2                    # 🟢 Creating Object

# s1 = student();
# print(s1.Course)
# print(s1.Branch)

#3                   # 🟢 Creating Constructor
# All Claas have a func called _init_(), which is always execute when the class is being inittiated. 

# class student:
#     Course = "BCA"
#     Branch = "CSE"
#     def __init__(self, fullName, marks): # parameter(self) iss compulsery.
#         self.name = fullName
#         self.marks = marks
#         print("adding new student in Dataabase...");

# s1 = student("Juned Khan", 97);
# print(s1.name, )
# print(s1.Course)
# print(s1.Branch)

# s2 = student("Zuned Khan", 99);
# print(s1.name, s2.marks)
# print(s1.Course)
# print(s1.Branch)


# 4                   # 🟢 Methode

# class student:
#     Course = "BCA"
#     Branch = "CSE"

#     def __init__(self, fullName, marks): # parameter(self) iss compulsery.
#         self.name = fullName
#         self.marks = marks
#         print("adding new student in Dataabase...");

#     def wekcome(self):
#         print("Welcome", self.name)

# s1 = student("Juned Khan", 97);
# s1.wekcome()
# print(s1.name, )
# print(s1.Course)
# print(s1.Branch)

# # ❓qtn:1

# class student:
#     def __init__(self, name, marks):
#         self.name =  name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi, your avg score is",sum/3)

# s1 = student("Zuned", [95, 99,93])
# print(s1.name)
# print(s1.marks)
# s1.get_avg()


# 5                    # 🟢 Static Methods

# class student:
#     @staticmethod  # decorater
#     def staticM():
#         print("Methods that don't use the self paraameter (work at class level)")

# s1 = student()
# s1.staticM()


