class Student:
    
    student_count = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__marks = 0

       
        Student.student_count += 1
        
    def add_marks(self, marks):
        self.__marks = marks

    def show_details(self):
        print("Name:", self.__name)
        print("Age:", self.__age)
        print("Marks:", self.__marks)
        print("-" * 20)

    @classmethod
    def total_students(cls):
        return cls.student_count

    @staticmethod
    def is_valid_age(age):
        return 5 <= age <= 25

if Student.is_valid_age(6):
    s1 = Student("Semira", 6)
    s1.add_marks(85)
    s1.show_details()

if Student.is_valid_age(20):
    s2 = Student("firdi", 20)
    s2.add_marks(92)
    s2.show_details()

print("Total Students:", Student.total_students())              
              