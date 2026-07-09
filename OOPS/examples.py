# expected output:
#name : Ravi
#age : 20
#marks : 50
#grade : A

# using abstract method 
from abc import ABC, abstractmethod
class Student_details(ABC):
    @abstractmethod
    def details(self):
        pass
class res(Student_details):
    def details(self, name, Age, Marks, grade):
        self.name = name
        self.age = Age
        self.marks = Marks
        self.grade = grade
        print("name: ", self.name)
        print("Äge : ", self.age)
        print("marks : ", self.marks)
        print("grade : ", self.grade)
    
Name = res()
Name.details("Ravi", 20, 50, "A")


# Using Polymorphism
class student_details:
    def details(self):
        pass
class name(student_details):
     def details(self, name, age, marks, grade):
        print("Name :", name)                   
        print( "age : ", age) 
        print("marks :", marks) 
        print("grade : ", grade)  

name1 = name()
name1.details("Spandana", 20, 50, "A")


# using inheritance 
class  student():
    def details(self,name, age):
        self.name = name
        self.age = age
        print("name :", name)
        print("age : ", age)
class result(student):
    def display(self, marks, grade):
        self.marks = marks
        self.grade = grade
        print("marks :", self.marks)
        print("grade : ",grade) 

result1 = result()
result1.details("Spandana", 21)
result1.display(20, "A")



# Encapsulation Example:
class student:
    def __init__(self,name, age, marks, grade):
        self.name = name    # public
        self.__age = age      # private
        self._marks = marks # protected
        self.grade = grade
    def details(self):
        print("name :", self.name)
        print("age: ", self.__age)
        print("marks :", self._marks)
        print("grade: ", self.grade)
result = student("spandana", 20, 70, "A")
result.details()




    

