# ✅ Abstraction, Encapsulation, Inheritance and Polymorphism is for mejor things for Oops.

# 6                   # 🟢 Abstraction

#Hiding the inplemntion details of a class and only share necassary faetures to the user.

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started...")

c_1 = Car()
c_1.start()


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


