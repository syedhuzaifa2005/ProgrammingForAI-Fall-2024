class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def display_student_details(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.name}")

class Marks(Student):
    def __init__(self, student_id, name, marks_algo, marks_data_science, marks_calculus):
        super().__init__(student_id, name)
        self.marks_algo = marks_algo
        self.marks_data_science = marks_data_science
        self.marks_calculus = marks_calculus

    def display_marks(self):
        print(f"Marks in Algorithms: {self.marks_algo}")
        print(f"Marks in Data Science: {self.marks_data_science}")
        print(f"Marks in Calculus: {self.marks_calculus}")

class Result(Marks):
    def display_result(self):
        total = self.marks_algo + self.marks_data_science + self.marks_calculus
        average = total / 3
        print(f"Total Marks: {total}")
        print(f"Average Marks: {average:.2f}")

student_result = Result(101, "Huzaifa", 85, 86, 93)
student_result.display_student_details()
student_result.display_marks()
student_result.display_result()
