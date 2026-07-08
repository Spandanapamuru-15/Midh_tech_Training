def welcome_message():
    print("Hello, Good Morning")
    print("MIDH TECH")
welcome_message()
welcome_message()



# prime number
def prime_number():
    num = int(input("Enter a number: "))
    if num <= 1:
        print("Entering Number is prime number")
        return 
    for i in range(2, num):
        if num % i == 0 :
            print("Entering Number is not prime number")
            return 
    print("prime")
prime_number()



# Using Arguments
def student_details(name, course):
    print("name: ", name)
    print("course: ", course)
student_details("spandana","AIML")
student_details("jaggu","CSE")


# adding elements using arguements
def add(a,b):
    return a + b
print("Addition of 2 numbers", add(10,20))
# substracting elements using arguemnets
def sub(a,b):
    return a - b
print("Substraction of 2 numbers is: ", sub(20,10))
# Multiplication elements using arguemnets
def mul(a,b):
    return a * b
print("Multiplication of 2 numbers is: ", mul(20,30))
# division  elements using arguemnets
def div(a,b):
    return a / b
print("Division of 2 numbers is: " ,div(20,30))



# using parameters & calculate prime number
# prime number
def prime_number(num):
    if num <= 1:
        return
    for i in range(2, num):
        if num % i == 0 :
           return "not prime"
    return  "is prime"
print(prime_number(3))


# Recursion
# Using Recursion Calculating factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print("Factorial of 6 is: ", factorial(6))


# taking input from user
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
n = int(input(("enter a number : ")))
print("Entering number factorial value is : ", factorial(n))