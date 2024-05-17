def fibonacci_series(n):
    fibonacci_series = [0, 1]
    for i in range(2, n):
        next_term = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_term)
    return fibonacci_series
n = int(input("Enter the number of terms: "))
print("Fibonacci series:", fibonacci_series(n))