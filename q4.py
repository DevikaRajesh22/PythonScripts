def checkNumber(n):
    status=n%2
    return status
num=int(input('Enter number to check :'))
k=checkNumber(num)
if k == 0 :
    print('Even')
else:
    print('Odd')