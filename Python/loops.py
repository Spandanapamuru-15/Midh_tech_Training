# loops for numbers
for number in range(1,6):
    print(number)

# While loop
count = 1
while count <= 3:
    print("while example code:", count)
    count += 1

seconds = 1
while seconds > 0:
    print("Timer:", seconds)
    seconds -= 1
print("Timer Finished")

#model 1
count = 1
while count <= 10:
    if count != 5 and  count != 6:
        print(count)
    count = count + 1

# model 2
for i in range(1,11):
    if i == 5 or i == 6:
        continue
    print(i)    

# using break stmt
for i in range(1,11):
    if i == 5 or i == 6:
        break
    print(i) 

#ordering food items
food = input("Enter your food item(press 'Q' to quit ) :")
while not food == 'q':
    print(f"you like {food}")
    food = input("Enter your another food item(press 'Q' to quit ) :")
print("Thank You")

num = int(input("Rate the food b/w 1-10: "))
while num < 1 or num > 10:
    print(f"{num} is invalid")
    num = int(input("Enter a number b/w 1-10: "))
print(f"You given Rating {num}")


# printing symbols
rows = int(input("Enter number of rows :"))
colomns = int(input("Enter number of colomns :"))
symbol = input("Enter your symbol :")
for i in range(rows):
    for j in range(colomns):
        print(symbol,end=" ")
    print()



# printing dail pad
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ["*", 0, "#"]
]

for row in numbers:
    for symbols in row:
        print(symbols, end=" ")
    print()









