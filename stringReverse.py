def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string
input_string = input("Enter a string: ")
print("Reversed string:", reverse_string(input_string))