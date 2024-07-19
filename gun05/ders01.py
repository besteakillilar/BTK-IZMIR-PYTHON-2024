# PYTHON RECURSIVE

def factorial(num):
    if num < 0:
        return "num must be positive"
        # raise ValueError("num must be positive")
    if num > 0:
        return num * factorial(num - 1)
    else:
        return 1

    #print(factorial(5))
