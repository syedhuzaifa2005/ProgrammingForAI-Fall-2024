inputlist=[]
numbers = int(input("Enter the number of digits: "))
x = 1
for i in range(numbers):
    numbers = int(input(f"Enter element {x}:" ))
    inputlist.append(numbers)
    x = x + 1
print(inputlist)

n = int(input("Enter the number: "))
filtered_list = [i for i in inputlist if i >= n]

print(filtered_list)