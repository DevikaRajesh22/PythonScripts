def oddToEven(L):
    for i in range(len(L)):
        if L[i] % 2 != 0:
            L[i] = L[i] ** 2
    print(L)

# Example usage
L = [1, 2, 3, 4, 5]
oddToEven(L)  # Output: [1, 2, 9, 4, 25]
