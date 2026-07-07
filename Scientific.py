### calculator program using if-elif-else statements
import math
operator = input("Enter the operator (+, -, *, /, **, %, sqrt, factorial, log, sin, cos, tan): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: ")) 
times = int(input("How many operations do you want : "))
if operator == '+':
    result = num1+num2
    print("After performing addition the result is :" ,result)
elif operator == '-':
    result = num1-num2
    print("After performing subtraction the result is:" ,result)
elif operator == '*':
    result = num1*num2
    print("After performing multiplication the result is:", result)
elif operator == '/':
    result = num1/num2
    print("After performing division the result is:" ,result)
elif operator == '**':
    result = num1 ** num2
    print("After Performing power calculation the result is:", result)
elif operator == '%':
    result = num1 % num2
    print("After Performing module calculation the result is:", result)
elif operator == 'sqrt':
    result = math.sqrt(num1)
    print("After Performing sqrt calculation the result is:", result)
elif operator == 'fact':
    print("After performing fact calculation ", math.factorial(int(num1)))
elif operator == 'log':
    print("After Performing log calculation ", math.log10(num1))  #output must be in common logarithm
elif operator == 'log':
    print("After Performing log calculation ", math.log10(num1)) #output must be in normal Algorithm
elif operator == 'sin':
    print("After Performing sin calculation ", math.sin(math.radians(num1)))
elif operator == 'Cos':
    print("After Performing Cos calculation the result is : ", math.cos(math.radians(num1)))
elif operator == 'tan':
    print("After performing tan calculation the result is : ", math.tan(math.radians(num1)))
else:
    print("Invalid Operator")
print("Do You Visit again :")
visit = input("Enter Yes or NO: ")
if visit.lower() == "yes":
    print("Do Calculation")
else:
    print("Thank You")
