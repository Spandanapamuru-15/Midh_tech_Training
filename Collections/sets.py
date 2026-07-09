"""numbers = {1,2,3,4,5,6,7,8,9,9,10,11,12,18,15,"Spandhu"}
print("Basic Example of Set is :", numbers)

# converting list to set
courses = ["python", " java", " python", "Devops", "java"]
unique_courses = set(courses)
print("Unique courses set is : ", unique_courses)


#example 
original_set = {104,101, 120, 2005}
print("Original set is:", original_set)
original_set.add(200)
print("After adding element set is :", original_set) # set method using add elements
original_set.remove(120)
print("After removing element is :", original_set)
print("Total values in set is :", len(original_set))"""


#Set Methods
s = {3372, 3374, 3371, 15, 2005}
print("original set is :", s)
s.add(17)
print("after using Add method : ", s)
s.update({30, 40})
print("After Update method is:", s)
s.remove(3374)
print(s)
s.discard(3372) #removing specific element
print(s)
s.pop()
print(s)
s.copy()
print(s)