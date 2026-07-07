# printing letter S
rows = 5
cols = 5

for i in range(rows):
    for j in range(cols):
        if (i == 0) or (i == 2) or (i == 4) or (i == 1 and j == 0) or (i == 3 and j == 4):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# printing letter P
rows = 6
cols = 6
for i in range(rows):
    for j in range(cols):
        if (i == 0) or (i == 2) or (j == 0) or (i == 0 and j == 5) or (i == 1 and j == 5):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print() 

#printing A letter
rows = 6
cols = 6
for i in range(rows):
    for j in range(cols):
        if ((i == 0 and j != 0 and j != 5) or (i == 2) or (j == 0 and i != 0) or (j == 5 and i != 0)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# printing N letter
rows = 6
cols = 6
for i in range(rows):
    for j in range(cols):
        if (j == 0) or (j == 5) or (i == 1 and j == 1) or ( i == 2 and j == 2) or ( i == 3 and j == 3) or ( i == 4 and j == 4):
             print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# Printing D letter
rows = 6
cols = 6
for i in range(rows):
    for j in range(cols):
        if (j == 0) or (i == 5 and j != 5) or (i == 0 and j != 5) or (i != 0 and j == 5 and i != 5) :
             print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# printing A letter
rows = 6
cols = 6
for i in range(rows):
    for j in range(cols):
        if ((i == 0 and j != 0 and j != 5) or (i == 2) or (j == 0 and i != 0) or (j == 5 and i != 0)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# printing N letter
rows = 6
cols = 6
for i in range(rows):
    for j in range(cols):
        if (j == 0) or (j == 5) or (i == 1 and j == 1) or ( i == 2 and j == 2) or ( i == 3 and j == 3) or ( i == 4 and j == 4):
             print("*", end=" ")
        else:
            print(" ", end=" ")
    print()




# printing A letter
rows = 6
cols = 6
for i in range(rows):
    for j in range(cols):
        if ((i == 0 and j != 0 and j != 5) or (i == 2) or (j == 0 and i != 0) or (j == 5 and i != 0)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


