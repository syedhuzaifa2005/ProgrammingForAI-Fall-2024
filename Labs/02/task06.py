num_elements = int(input("Enter the number of elements you want to store in the list: "))
elements_list = []
for i in range(num_elements):
    element = int(input(f"Enter element {i+1}: "))
    elements_list.append(element)

def multiply_list(_list):
    result = 1
    for element in _list:
        result *= element
    return result

print("The product of all elements in the list is", multiply_list(elements_list))