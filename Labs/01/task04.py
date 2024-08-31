inputlist=[]
numbers = int(input("Enter the number of digits: "))
for i in range(numbers):
    numbers = int(input("Enter the number: "))
    inputlist.append(numbers)
print(inputlist)
sum = 0

for i in inputlist:
    sum = sum + i

print(sum)
