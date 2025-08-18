#----------------------->>>>>>>>>String in PYTHON<<<<<------------------............

str1 = "this is 'string' 1"
str2 = 'this is "string" 2'
str3 = """this is string 3
it is multiline string"""

a = "Hello, World!"
print(a[1]) #acess idx 1

for x in "banana":
  print(x)            # printing all value

print(len(a))         # string length is 13



#finding in string =>

txt = "The best things in life are free!"
print("free" in txt)                              # in

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")          # not in



# Slicing a String =>

b = "Hello, World!"
print(b[2:5])                          #llo
print(b[:5])                           # from 0th element to 5th 
print(b[2:])                           #from 2th to end
print(b[-5:-2])                        #from last word of string

## some functions in python :

str = "Internation Islam Univarsity Chittagong"

print(str.endswith("gong"))     #return true if it's ends with this substr

print(str.capitalize())         #first latter will be capitalized
print(str.upper())              #printing upper case
print(str.lower())              #printing lower case
print(str.find("e"))            #return the first index of e
print(str.replace("t", "T"))    #replace letter
print(str.count("i"))           #return the total occurencen of the substr

print(str.strip())       #method removes any whitespace from the beginning or the end:
print(str.split(","))           # returns ['Hello', ' World!']

# concatnation :
str
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#  combine strings and numbers by using f-strings method!

price = 59
txt = f"The price is {price} dollars"
Txt = f"The price is {20 * 59} dollars"
print(txt)
print(Txt)

