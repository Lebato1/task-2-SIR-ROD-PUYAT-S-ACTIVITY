class Student:
   
    def __init__(self, student_name, student_age, student_course):
       
        if not isinstance(student_name, str):
            raise TypeError("Student name must be a string.")
        if not isinstance(student_course, str):
            raise TypeError("Student course must be a string.")
        if not isinstance(student_age, int) or student_age < 0:
            raise ValueError("Student age must be a non-negative integer.")


        self.name = student_name 
        self.age = student_age
        self.course = student_course  
       
        print(f"A new Student object has been created: Name - {self.name}, Age - {self.age}, Course - {self.course}")

    def introduce(self):
       
        print("--------------------") 
        print(f"Hello, my name is {self.name}.")
        print(f"I am {self.age} years old.")
        print(f"I am taking the {self.course} course.")
        print("--------------------")  

student1 = Student("ramil", 20, "IT")
student2 = Student("gibea", 21, "IT")
student3 = Student("Junko",22, "IT")

print("\nStudent 1 Introduction:")
student1.introduce()

print("\nStudent 2 Introduction:")
student2.introduce()

print("\nStudent 3 Introduction:")
student3.introduce()