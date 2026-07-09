"""class Animal:
    def eat(self):
        print("Animal eats food")

class Dog(Animal):
    def bark(self):
        print("Dog Barks")

dog1 = Dog()
dog1.eat()
dog1.bark()


class Animal:
    def eat(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog Barks")

dog1 = Dog()
dog1.eat()
dog1.bark()"""

# Hierarichal Inheritance
class Animal:
    def eat(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog Barks")

class cat(Animal):
    def bark(self):
        print("cat Barks like Meoww....")

class Lion(Animal):
    def bark(self):
        print("Lion Barks like Roar....")
class Duck(Animal):
    def bark(self):
        print("Duck Barks like Quak Quak....")

dog1 = Dog()
cat1 = cat()
lion1 = Lion()
duck1 = Duck()
dog1.eat()
dog1.bark()
cat1.bark()
lion1.bark()
duck1.bark()


# single Inheritance
class  student():
    def courses(self):
        pass
class result(student):
    def display(self, course):
        self.course = course
        print("course : ", course) 

result1 = result()
result1.display("Python")

#multple inheritance
class Topper:
    def class1(self):
        print("FIrst Division")

class Backbencher:
    def class2(self):
        print("Second Division")

class Child(Topper, Backbencher):
    pass

c = Child()
c.class1()
c.class2()


# multilevel inheritance
class student:
    def name(self):
        print("Name : Spandana")

class marks(student):
    def marks(self):
        print("Marks : 95")

class result(marks):
    def grade(self):
        print("Grade : A")

student1 = result()

student1.name()
student1.marks()
student1.grade()

# hybrid inheritance
class Student:
    def name(self):
        print("Name : Spandana")
class Marks(Student):
    def marks(self):
        print("Marks : 95")
class Sports(Student):
    def sports(self):
        print("Sports Grade : A+")
class Result(Marks, Sports):
    def result(self):
        print("Result : Pass")
student1 = Result()
student1.name()   
student1.marks()   
student1.sports()  
student1.result() 