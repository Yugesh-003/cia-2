class Student:
    def calculate_marks(self, marks):
        return sum(marks)  # Default total marks calculation

class EngineeringStudent(Student):
    def calculate_marks(self, marks):
        return sum(marks) / len(marks)  # Average marks for an engineering student

class MedicalStudent(Student):
    def calculate_marks(self, marks):
        return max(marks)  # Highest mark for a medical student

# Creating objects
eng_student = EngineeringStudent()
med_student = MedicalStudent()
gen_student = Student()

marks = [80, 90, 85, 70, 95]

# Calling overridden methods
print("Total Marks (General Student):", gen_student.calculate_marks(marks))
print("Average Marks (Engineering Student):", eng_student.calculate_marks(marks))
print("Highest Marks (Medical Student):", med_student.calculate_marks(marks))
