#ERRORS

try:
    a = int(input("Enter a number: "))
    print(a)
    # k = a/0
    z = "q" / "w"
except ValueError:
    print("Error")
except ZeroDivisionError:
    print("Error division by zero")
except Exception as e:
    print("Error type : ", e)
