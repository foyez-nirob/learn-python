#----------------------->>>>>>>>>LOOP IN PYTHON<<<<<------------------............

##  while condition :
        # work

count = 0

while count<=5:
    print("hello world")
    count+=1

list = [1,2,3,4,5,6,7,8,10]
x = 5
i = 0
while i < len(list):
    print(list[i])
    i+=1
    if x == list[i]:
        break



#     for loop ==>      

ll = [2,3,4,5,6,7]

for el in ll :
    print(el)




str = "helloWorld!"
for el in str :
    print(el)
else :
    print("end")



## Range function i python ==>
# * range function returns a sequence of numbers starting from 0 and increment by 1
# by (defauts) and stops before a specific number
# range(start?,stop,step?)

seq = range(5)
print(seq[0])
print(seq[1])
print(seq[2])

for i in seq :
    print(i)

for i in range(5):
    print(i)

for i in range(2,5):            #start from 2 and stop before 5
    print(i)

for i in range(2,10,2):
    print(i)

for i in range(5):
    pass                        # skip the works

n = 10
sum = 0
for i in range(n):
    sum +=(i)
print (sum)



#----------------------->>>>>>>>>FUNCTION IN PYTHON<<<<<------------------............

# def function_name(para1,para2,...):
    # return value

# function_name(argu1,argu2)  for call the function


def sum(a,b):
    sum = a+b
    return sum

print(sum(5,5))

def print_hello():
    print("hello")

print_hello()


def sum2(a=1,b=2):                    #defaut function when argument are not passed
    print(a+b)

sum2()


def lenth(list):
    count = 0
    for x in list :
        count = count+1
    return count 

list = [1,2,3,4,5]
print(lenth(list))



def factorial(n):
    res = 1
    for i in range(1,n+1):
        res = res*i
    return res

print(factorial(5))

def even_odd(n):
    if(n%2 == 0):
        return "this is even number"
    else:
        return "this is odd number"

print(even_odd(5))

#----------------------->>>>>>>>>RECURSSION IN PYTHON<<<<<------------------............

def show(n):
    if(n==0):
        return
    print(n,end=" ")
    show(n-1)

show(5)                 # 5 4 3 2 1
print()

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

print(fact(5))

def sum3(n):
    if(n==0):
        return 0
    else:
       return n + sum3(n-1)

print(sum3(5))

def revprint(ll,n):
    if(n==0):
        return
    print(ll[n-1],end=" ")
    revprint(ll,n-1)

ll = [1,2,3,4,5]
revprint(ll,len(ll))
print()