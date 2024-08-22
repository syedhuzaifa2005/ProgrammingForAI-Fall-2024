physics = float(input("Enter physics marks: "))
chemistry = float(input("Enter chemistry marks: "))
maths = float(input("Enter maths marks: "))

marks_dict = {
    "Physics" : physics,
    "Chemistry" : chemistry,
    "Maths" : maths
}

average_marks = sum(marks_dict.values()) / len(marks_dict)
highest_marks = max(marks_dict, key=marks_dict.get)

print("Average Marks: ", average_marks)
print("Highest Marks in: ", highest_marks)