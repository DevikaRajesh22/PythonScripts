def reverse(num):
    rev = 0
    while num > 0:
        rem = num % 10 # extract last digit
        rev = rev * 10 + rem # update rev with last digit
        num = num // 10 # removes last digit from num by performing  integer division
    return rev

print(reverse(1234))

'''
Initial state: num = 1234, rev = 0

First iteration:
    rem = 1234 % 10 = 4
    rev = 0 * 10 + 4 = 4
    num = 1234 // 10 = 123
    
Second iteration:
    rem = 123 % 10 = 3
    rev = 4 * 10 + 3 = 43
    num = 123 // 10 = 12
    
Third iteration:
    rem = 12 % 10 = 2
    rev = 43 * 10 + 2 = 432
    num = 12 // 10 = 1

Fourth iteratio:
    rem = 1 % 10 = 1
    rev = 432 * 10 + 1 = 4321
    num = 1 // 10 = 0
'''