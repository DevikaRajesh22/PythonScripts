# Global variable
global_var = 10

def func():
    print("Inside func(), global_var:", global_var)

def another_func():
    global global_var
    global_var = 20
    print("Inside another_func(), global_var:", global_var)

func()
another_func()
print("Outside all functions, global_var:", global_var)
