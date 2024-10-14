import numpy as np

dtype = [('name', 'U10'), ('height', 'f4'), ('class', 'i4')]

students = np.array([
    ('Sabeeh', 5.5, 10),
    ('Haris', 5.9, 9),
    ('Rayyan', 5.6, 10),
    ('Huzaifa', 6.2, 9)
], dtype=dtype)

sorted_students = np.sort(students, order=['class', 'height'])
print(sorted_students)
