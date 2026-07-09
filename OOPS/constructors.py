class student:
    def __init__(self, name, age, course, ID):
        self.name = name
        self.age = age
        self.course = course
        self.ID = ID
    def display(self):
        print("name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("ID :", self.ID)
s1 = student("Spandana", 21, "AIML", 3371)
s1.display()
s2 = student("jaggu", 19, "CSE", 3374)
s2.display()