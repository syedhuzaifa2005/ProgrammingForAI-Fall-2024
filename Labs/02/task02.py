def check_last_letter(input_string):
    vowels = 'aeiouAEIOU'
    
    input_string = input_string.strip()

    if not input_string:
        return "The input string is empty."
    
    last_char = input_string[-1]
    
    if last_char in vowels:
        return f"The last letter '{last_char}' is a vowel."
    else:
        return f"The last letter '{last_char}' is a consonant."

user_input = input("Enter a string: ")
result = check_last_letter(user_input)
print(result)