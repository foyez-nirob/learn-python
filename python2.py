#---->>>>>>>> String <<<<<<<-------

a = "Hello, World!"
print(a[1]) #acess idx 1

for x in "banana":
  print(x)    # printing all value

print(len(a)) # string length is 13

#finding in string =>

txt = "The best things in life are free!"
print("free" in txt)                       # in

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")  # not in

# printing element from string =>

b = "Hello, World!"
print(b[2:5]) #llo
print(b[:5])  # from 0th element to 5th 
print(b[2:]) #from 2th to end
print(b[-5:-2]) #from last word of string

## some functions in python :

a = " Hello, World!"

print(a.upper())   #printing upper case
print(a.lower())   #printing lower case
print(a.strip())   #method removes any whitespace from the beginning or the end:

print(a.replace("H", "J"))    #replace letter
print(a.split(","))        # returns ['Hello', ' World!']


# concatnation :

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

