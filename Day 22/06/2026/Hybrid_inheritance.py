# ==========================================
# HYBRID INHERITANCE IN PYTHON
# ==========================================

# Parent class
class Person:

    def show_person(self):
        print("I am a person")


# Child class of Person
class Student(Person):

    def show_student(self):
        print("I am a student")


# Another child class of Person
class Teacher(Person):

    def show_teacher(self):
        print("I am a teacher")


# Child class inherits from Student and Teacher
# This is multiple inheritance
class TeachingAssistant(Student, Teacher):

    def show_ta(self):
        print("I am a teaching assistant")


# Create object of TeachingAssistant
ta = TeachingAssistant()

# Method from Person
ta.show_person()

# Method from Student
ta.show_student()

# Method from Teacher
ta.show_teacher()

# Method from TeachingAssistant
ta.show_ta()
