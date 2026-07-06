myVariableName = "Spandana"  # pascal case
MyVariableName = "Pamuru" #camel case
my_variable_name = "Python" #snake case
print(myVariableName)
print(MyVariableName)
print(my_variable_name)

#Using variables in expressions
age = 25
print("present age is", age)

#print student name and age and course
student_name = "Spandana"
student_age = 21
student_course = "Python"
print("Student name is", student_name, "age is", student_age, "course is", student_course)

# calculating Fee details 
students = 30
Course_fee = 100
fee_paid_students = 12
fee_per_student = 4000
fee_unpaid_students = students - fee_paid_students
print("Total fee is", fee_paid_students * Course_fee)
print("Unpaid fee is", fee_unpaid_students * Course_fee)
total_collection = fee_paid_students * fee_per_student
print("Total collection is", total_collection)

# USING F STRINGS
name = "spandana"
age = 21
college_name = "GIST"
Joining_Comapany = "MIDH TECH"
joining_year = 2026
print(f"my name is {name}")
print(f"my age is {age}")
print(f"my college name is {college_name}")
print(f"I have joined company is {Joining_Comapany}", f" and joining_year is {joining_year}")


# Using BOOLEAN Data type
student_name = "Spandana"
loggin_status = True
if loggin_status:
    print("True",f" Student_name is {student_name}")
else:
    print("false", f"student_name is{student_name}")
print(f"Type: {type(student_name)}")
print(f"Type {type(loggin_status)}")


name = "Spandana"
age = 21
marks = 94.7
if age > 18:
    print("True")
else:
    print("False")
print(name, f"type:{type(name)}")
print(age, f"type:{type(age)}")
print(marks, f"type:{type(marks)}")


#TYPE CASTING


a = 10
print(f"Type of a is {type(a)}")
print(f"Boolean value of a is {bool(a)}")
print(f"type:{type(bool(a))}")

a = 20
print(f"Type of a is {type(a)}")
if a == 20:
    print("true")
else:
    print("false") 

# Taking input from user 
name = input("Enter your name : ")
age = int(input("Enter your age : "))
company_name = input("Enter your company name : ")

# Taking input from user and printing the details
name = input("Enter your name : ")
age = int(input("Enter your age : "))
company_name = input("Enter your company name : ")
print("name is:", name)
print("age is:", age)
print("company_name is:", company_name) 

# calculating the area of rectangle
length = int(input("Enter the length of rectangle :"))
width = int(input("Enter the width of rectangle : "))
area = length * width
print("Area of rectangle is : ", area)


# Operators in python
name = input("Enter your name :")
roll_number = int(input("Enter your roll number :"))
Subject1=int(input("Enter your marks in subject1 :"))
Subject2=int(input("Enter your marks in subject2 :"))
Subject3=int(input("Enter your marks in subject3 :"))
Subject4=int(input("Enter your marks in subject4 :"))
Subject5=int(input("Enter your marks in subject5 :"))
Subject6=int(input("Enter your marks in subject6 :"))
total_marks = Subject1 + Subject2 + Subject3 + Subject4 + Subject5 + Subject6
percentage = (total_marks/600)*100
print("Total marks is :", total_marks)
print("Percentage of all subjects is :", percentage)

# Assignment operators
wallet = 1000
wallet += 500
wallet -= 200
print("final wallet balance is :", wallet)


# Comparison operators
my_balance = 1000
my_frnd_balance = 2000
if my_balance == my_frnd_balance:
    print("True")
else:
    print("False")
if my_balance != my_frnd_balance:
    print("True")


# using print statements to check the comparison operators
my_balance = 1000
my_frnd_balance = 2000
print("my_balance is equal to my_frnd_balance :", my_balance == my_frnd_balance)
print("my_balance is not equal to my_frnd_balance :", my_balance != my_frnd_balance)
print("my_balance is greater than my_frnd_balance :", my_balance > my_frnd_balance)
print("my_balance is less than my_frnd_balance :", my_balance < my_frnd_balance)

## Logical operators
marks = int(input("Enter your marks :"))
if marks >= 35 and marks <= 100:
    print("Pass")
elif marks < 35 and marks >= 0:
    print("Fail")
else:
    print("Invalid marks")

marks = int(input("Enter your marks :"))
if marks >= 35 or marks <= 100:
    print("Pass")
elif marks < 35 or marks >= 0:
    print("Fail")
else:
    print("Invalid marks")


#identity operators
basket1 = ["apple", "banana", "orange"]
basket2 = ["apple", "watermelon", "Mango"]
if basket1 is basket2:
    print("True")
else:
    print("False")



# is not operator
basket1 = ["apple", "banana", "orange"]
basket2 = ["apple", "banana", "orange"]
if basket1 is not basket2:
    print("True")
else:
    print("False")

cart=["apple", "banana", "orange"]
same_cart=cart
new_cart=["apple", "banana", "orange"]
print("same_cart is cart :", same_cart is cart)
print("new_cart is cart :", new_cart is cart)

# Membership operators
cart=["apple", "banana", "orange"]
search_fruit = "orange"
print("search fruit is in cart :", search_fruit in cart)
print("search fruit is not in cart :", search_fruit not in cart)


## Bitwise operators
# using AND operator
READ = 1 #binary 001
WRITE = 2 #binary 010
EXECUTE = 4 #binary 100
user_permission = READ | WRITE  # combine read and write permissions.
print("can read :",bool(user_permission & READ))
print("can write :",bool(user_permission & WRITE))
print("can execute :",bool(user_permission & EXECUTE))

##bitwise OR operator
READ = 1 #binary 001
WRITE = 2 #binary 010
EXECUTE = 4 #binary 100
user_permission = READ | WRITE  # combine read and write permissions.
print("can read :",bool(user_permission | READ))
print("can write :",bool(user_permission | WRITE))
print("can execute :",bool(user_permission | EXECUTE))

##finding min and max values
numbers = [10, 20, 30, 40, 50]
print("Minimum value in numbers list is :",min(numbers))
print("Maximum value in numbers list is :",max(numbers))


a = 10
b = 22
c = 50
if a > b and a > c:
    print("a is maximum value")
elif b > a and b > c:
    print("b is maximum value")
else:
    print("c is maximum value")

if a < b and a < c:
    print("a is minimum value")
elif b < a and b < c:
    print("b is minimum value")
else:
    print("c is minimum value")

# using if-elif-else staments
if True:
    if 10 > 5:
        print("Basic example: nested condition passed")
age  = 21
citizen = True
if age >= 18:
    if citizen:
        print("simYou are eligible to vote")
    else:
        print("simple program: citizenship required")
else:
    print("simple program: age should be 18 or above")

### calculator program using if-elif-else statements
operator = input("Enter the operator (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if operator == '+':
    result = num1+num2
    print("After performing addition the result is :" ,result)
elif operator == '-':
    result = num1-num2
    print("After performing subtraction the result is:" ,result)
elif operator == '*':
    result = num1*num2
    print("After performing multiplication the result is:", result)
elif operator == num1/num2:
    result = num1/num2
    print("After performing  division the result is:" ,result)
else:
    print("Invalid Operator")


# Validation form
Username = input("Enter your name: ")
password = input("Enter Your password : ")
if Username != " ":
    if len(password) >= 8:
        if("@" in password or "#" in password or "$" in password or "%" in password or "&" in password or "*" in password or "!" in password): 
             print("Login Successful")
        else:
            print("Error: Password must contain at least one special character.")
    else:
        print("Error: Password must be at least 8 characters long.")
else:
    print("Error: Name cannot be empty.")



