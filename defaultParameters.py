# Calling the function with and without providing the greeting argument

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))
print(greet("Alice", "Hi"))