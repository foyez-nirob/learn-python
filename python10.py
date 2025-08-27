#----------------------->>>>>>>>>INHERITANCE AND POLYMORPISM<<<<<------------------............

#single level inheritance :

class car:
    @staticmethod
    def start():
        print("car starting....buuuu")
    
    @staticmethod
    def stop():
        print("car stoping ... breeeeeakkk")
    
class toyota(car):
    def __init__(self,name):
        self.name = name
        super().start()
    

car1 = toyota("kala car")
print(car1.name)

car1.start()
car1.stop()


# Multiple inheritance :

class A:
    val1 = "this is class a"
class B:
    val2 = "this is class b"
class C(A,B):
    val3 = "this is class c"
    

obj = A()
print(obj.val1)

#class method :

class person:
    name = "anonymous"

    # def change_name(self,name):
    #     # person.name = name 
    #     # self.__class__.name =name 

    @classmethod
    def change_name(cls,name):
        cls.name = name 
    
p = person()
p.change_name("nirob")
print(p.name)
print(person.name)

#property method ==>

class marks:
    def __init__(self,py,chem,math):
        self.phy = py 
        self.chem = chem
        self.math = math 
    
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"

m = marks(98,98,97)
print(m.percentage)

m.phy = 33
print(m.percentage)

## Polymorpism ==>

class Complex:
    def __init__(self,i,j):
        self.i = i 
        self.j = j
    def show(self):
        print(self.i,"i +",self.j,"j")
    
    def __add__(self,num):
        new_i = self.i + num.i
        new_j = self.j + num.j
        return Complex(new_i,new_j)


num1 = Complex(2,3)
num2 = Complex(4,5)
num3 = num1 + num2
# num3 = num1.__add__(num2)
num3.show()



### practice oop concepts ::

class Employ:
    def __init__(self,role,salary,dept):
        self.role = role
        self.salary = salary
        self.dept = dept 
    
    def show_details(self):
        print("role: ",self.role)
        print("salary :",self.salary)
        print("department: ",self.dept)

class Engineer(Employ):
    def __init__(self,name,age,role, salary, dept):
        self.name = name 
        self.age = age
        super().__init__(role, salary, dept)
    
    def show_details(self):
        print("name :",self.name)
        print("age :",self.age)
        super().show_details()

eng = Engineer("elon",40,"chef",1000000,"science")
eng.show_details()