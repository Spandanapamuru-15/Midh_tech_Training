class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class cat(Animal):
    def sound(self):
        print("cat meows...")

animals = [Animal(), Dog(), cat()]

for animal in animals:      # the same method name calls different implementation
    animal.sound()

def add(a, b = 0, c = 0):    
    return a + b + c

print("add(5):", add(5))
print("add(5, 10): ", add(5, 10))
print("add(5,10,15): ", add(5,10,15))



# Polymorphism
class student_details:
    def details(self):          # method overriding
        pass
class name(student_details):
     def details(self, name, age, marks, grade):
        print("Name :", name)                   
        print( "age : ", age) 
        print("marks :", marks) 
        print("grade : ", grade)  

name1 = name()
name1.details("Spandana", 20, 50, "A")



# method overloading
