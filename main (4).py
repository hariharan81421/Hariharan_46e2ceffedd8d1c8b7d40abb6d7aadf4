class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Example usage:
student1 = Student("Alice", "A001", 3.8)
student2 = Student("Bob", "B002", 3.5)
student3 = Student("Charlie", "C003", 3.7)

student_list = [student1, student2, student3]
sorted_list = sort_students(student_list)

for student in sorted_list:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
  