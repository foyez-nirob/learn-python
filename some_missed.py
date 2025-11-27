
total_price = 100 #snake_case_variable
totalPrice = 100 #camelCaseVariable
TotalPrice = 100 #PascalCaseVariable

print("hello world")

a = 5
b = 3

print(a**b) # Exponentiation: 5 raised to the power of 3

#operators precedence
# (BODMAS)
# 1. Parentheses( )
# 2. Exponentiation(**)
# 3. Multiplication and Division and modulus(*, /, %)
# 4. Addition and Subtraction(+, -)
# 5. Comparison Operators(==, !=, >, <, >=, <=)
# 6. Logical Operators(not , and, or)
#if there is same precedence then we will go from left to right

# match case statement (it's like switch case in other languages)

day = "Monday"

match day:
    case "Monday":
        print("It's Monday")
    case "Tuesday":
        print("It's Tuesday")
    case _:
        print("It's some other day")


def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

print(fact(5))