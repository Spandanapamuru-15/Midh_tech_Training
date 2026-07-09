""""double = lambda X: X * 2          # lambda doubles a number(like multiplication)
print("After performing lambda function the result is :", double(5))"""

marks = [70, 80, 90]
bonus_marks = list(map(lambda mark: mark + 5, marks))
print("Bonus marks: ", bonus_marks)

marks = [20, 35, 60, 30, 90]
bonus_marks = list(filter(lambda mark: mark >= 35, marks))
print("Bonus marks: ", bonus_marks)



from functools import reduce
marks = [2, 4, 5, 7,8]
bonus_marks = reduce (lambda X,Y : X * Y, marks)
print("Bonus Marks: ", bonus_marks)