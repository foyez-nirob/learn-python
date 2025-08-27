#----------------------->>>>>>>>>OOP in PYTHON<<<<<------------------............

#class is the blueprint of objects 

class Student:                      # this is a class
    name = "python"

obj = Student()                     # this is an objects
# print(obj.name)


#===> constructor :

class car:
    def __init__(self):
        print("this is constructor")

s = car()

class Name:
    school = "apna college"
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def get_name(self):
        print("your name is ",self.name)
    def get_marks(self):
        print("your marks is ",self.marks)

s1 = Name("nirob",97)
print(s1.name)
print(s1.marks)
print(s1.school)

s1.get_name()
s1.get_marks()

s2 = Name("ironman",48)
del s2                      # deleting the object


## Static method ===>>  
class hello:
    @staticmethod
    def hello():
        print("hello broh")


s = hello()
s.hello()

#practice problem ::--->

class Account:
    def __init__(self,acc_no,bal):
        self.__account_no = acc_no          # method to private a atribute : __ at the first of the atribute 
        self.balance = bal
    
    def debit(self,amount):
        self.balance -= amount
        print(amount,"tk balance is debited form the acc")
        self.__show()
    
    def credit(self,amount):
        self.balance += amount
        print(amount,"tk balance is credited form the acc")
        self.__show()
   
    def __show(self):                   # this  method is private now 
        print("total amount of your account is",self.balance)

    

person = Account(12223,5000)
person.credit(5000)
person.debit(300)

