import matplotlib.pyplot as plt

math_marks = [85, 78, 91, 83, 76, 95, 89, 72, 91, 83]
science_marks = [80, 75, 90, 85, 70, 93, 88, 78, 94, 82]

plt.scatter(math_marks, science_marks, color='blue', label='Students')
plt.xlabel('Mathematics')
plt.ylabel('Science')
plt.title('Scatter Plot: Mathematics vs Science Marks')

plt.legend()
plt.show()
