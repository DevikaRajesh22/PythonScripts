def factorial(number):
    factorial_result = 1
    for i in range(1, number + 1):
        factorial_result *= i
    return factorial_result
number = int(input("Enter a number:"))
print("Factorial:", factorial(number))