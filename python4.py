#----------------------->>>>>>>>>condition<<<<<------------------............


# python input:

name = input("give your name :")
age = int(input("give your age  :"))
print(name)
print(age+2)
print("my name is :",name,"my age is :",age)

# Python condition

marks = int(input("give marks :"))

if(marks >= 80):
    print("A+")
elif(marks >= 70 ):
    print("A")    
else:
    print("tui fail")

# Python ternary

#method 1 ->

food = input("food name : ")
eat ="yes" if(food =="cake") else "no"
print(eat)

#method 2 ->
print("sweet") if (food =="cake") or (food =="jelebi") else print("tok")

#method 3 -->

age = int(input("give your age : "))
under_age = ("yes","no") [age>=18]
print(under_age)

salary = float(input("give your salary"))
tax = salary*(0.1,0.2) [salary>=5000]
print(tax)


