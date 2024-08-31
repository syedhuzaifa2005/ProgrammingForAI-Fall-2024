import random

num = 30
temperatures_list = []
for i in range(num):
    random_num = round(random.uniform(25.0, 60.0), 2)
    temperatures_list.append(random_num)

def calc_avg(_list):
    _sum = 0
    _sum = sum(_list)
    avg = _sum / len(_list)
    return avg

def max_min_values(_list):
    max_value = max(_list)
    min_value = min(_list)
    print("The highest temperature for this month is", max_value, "⁰C")
    print("The lowest temperature for this month is", min_value, "⁰C")

def sort_list_remove_element(_list):
    sorted_list = sorted(_list)
    print("Sorted List:\n", sorted_list)
    n = int(input("Enter a number between 0 and 29: "))
    if(n > 29  or  n < 0):
        exit(0)
    else:
        del sorted_list[n]
    print("Sorted list after removing element:\n", sorted_list)


print("The average temperature for this month is", calc_avg(temperatures_list), "⁰C")
max_min_values(temperatures_list)
print("The sorted list in ascending order is:\n", sort_list_remove_element(temperatures_list))
