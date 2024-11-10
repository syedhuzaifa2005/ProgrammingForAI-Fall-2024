import matplotlib.pyplot as plt

student_ages = [18, 27, 23, 30, 28, 19, 18, 31, 42, 21, 28, 27, 19, 39, 22, 21, 36, 37, 40, 19]

age_groups = ['18-25', '26-30', '31-35', '36 and above']


group_18_25 = sum(1 for age in student_ages if 18 <= age <= 25)
group_26_30 = sum(1 for age in student_ages if 26 <= age <= 30)
group_31_35 = sum(1 for age in student_ages if 31 <= age <= 35)
group_36_above = sum(1 for age in student_ages if age >= 36)


student_counts = [group_18_25, group_26_30, group_31_35, group_36_above]
plt.pie(student_counts, labels=age_groups, autopct='%1.1f%%', startangle=140, colors=['#ffcc99', '#ff9966', '#99cc99', '#66b3ff'])
plt.title('Distribution of Student Ages')
plt.show()
