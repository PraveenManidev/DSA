class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age 
        self.grade = grade 
    def get_grade(self):
        return self.grade 

class Course:
    def __init__(self,name,max_students):
        self.name = name 
        self.max_students = max_students
        self.students = []

    def add_student(self,student):
        if(len(self.students)<self.max_students):
            self.students.append(student)
            return True 
        return False 
    
    def average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        value = value / len(self.students)
        return value


s1 = Student('Tim',18,90)
s2 = Student('Praveen',25,95)

course = Course("science",2)
course.add_student(s1)
course.add_student(s2)

print(course.students[1].grade)
print(course.average_grade())



















'''class Dog:
    def __init__(self, name,age): #This will be called whenever a object has been instantiated.
        self.name = name 
        self.age = age 

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self,age):
        self.age = age

d = Dog('Praveen',23)
print(d.get_name())
d2 = Dog('Vijay',15)
print(d.get_age())
print(d2.get_name())
d.set_age(2)
print(d.get_age())'''