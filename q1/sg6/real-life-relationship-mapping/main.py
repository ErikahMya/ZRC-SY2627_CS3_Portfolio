# Write a short Python code snippet showing a Course adding a Student object to a list. 
 class Student:
    def __init__(self, name, student_id):
        self.__name = name
        self.__student_id = student_id

    def get_info(self):
        return self.__name
 
 class Course:
    def __init__(self, course_name):
        self.__course_name = course_name
        self.__students = []

    def add_students(self, student):
        self.__students.append(student)