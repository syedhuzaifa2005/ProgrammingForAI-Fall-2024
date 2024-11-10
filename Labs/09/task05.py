import matplotlib.pyplot as plt

student_genders = ['Male', 'Female', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male']

gender_counts = [student_genders.count('Male'), student_genders.count('Female')]

plt.pie(gender_counts, labels=['Male', 'Female'], autopct='%1.1f%%', startangle=140, colors=['#66b3ff', '#ff66b3'])
plt.title('Gender Distribution of Students')
plt.show()
