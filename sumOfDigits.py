def sum_of_digits(number):
    # Initialize sum variable to store the sum of digits
    digit_sum = 0
    # Iterate through each digit of the number
    while number > 0:
        # Extract the last digit of the number
        digit = number % 10
        # Add the digit to the sum
        digit_sum += digit
        # Remove the last digit from the number
        number //= 10
    return digit_sum

number = int(input("Enter an input : "))
print("Sum of digits :", sum_of_digits(number))