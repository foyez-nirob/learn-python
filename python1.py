#----------------------->>>>>>>>>PYTHON JOURNEY<<<<<------------------............


# printing first code:

print("hello world")
print("helloo coders !")

#indentation matter here 

if 5>3 :
    print("it's correct")
    print("it's also correct")
#        print("it's not correct")

## variables :

x = 5
y = "hello"

print(x) # 5
print(y) # hello

x = 5 
x = "hello"

print(x) # hello 

## type casting 

x = str(3)
y = int(3)   
z = float(3) # 3.0

#we can also see the type 

x = 3
y ="hello"

print(type(x))
print(type(y))

#we can declare string by single qoute

x = "hello"
y = 'hello y'

print(x)
print(y)

# case sensitive 

a = 10
A = "hello"
#* they are different variable

print(a) # 10
print(A) # hello

# Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# multi assignment 

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x) #orange
print(y) #orange
print(z) #orange

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x) #apple 
print(y) #banana
print(z) #cherry

## Outputs system 

x = 3
y = 9.99
z = "awesome"
print(x, y, z) #3 9.99 awesome

x = "Python "
y = "is"
z = "awesome"
print(x + y + z) #python isawesome

print("hello",10,3.1416) #hello 10 3.1416

## local variable vs global variable

x = "awesome" #-> global variable

def myfunc():
  x = "fantastic" #-> local variable
  print("Python is " + x)

myfunc()

print("Python is " + x)

#--
x = "awesome"

def myfunc():
  global x                  #creating global variable that can override
  x = "fantastic"

myfunc()

print("Python is " + x)

## python Number :

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

y = int(2.8) # y will be 2
z = int("3") # z will be 3

y = float(2.8)   # y will be 2.8
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'


## Python string ##

print("It's alright")
print("He is called 'Johnny'") #* system of using quote inside string ;
print('He is called "Johnny"')

# assign multiline string we need to use 3(three) quotes(single or double)
a = """Lorem ipsum dolor sit amet,    
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) 
