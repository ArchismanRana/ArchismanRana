
def factorial(n):
    if n < 0:
        f = 0
        return f
    elif n == 0:
        f = 1
        return f
    else:
        f = 1
        for i in range(1, n + 1):
            f = f * i
        return f


# __main__
while True:
    num = eval(input("Enter a number :"))
    if isinstance(num, float):
        print("Factorial exists for int type numbers not for decimals.")
    elif isinstance(num, int):
        if factorial(num) == 0:
            print("Factorial does not exist")
        else:
            print("The factorial of ", num, " is ", factorial(num))

    Repeat_Process = input("Do you want to find factorial of another number (Yes/No): ")
    if Repeat_Process == "Yes" or Repeat_Process == "yes":
        continue
    else:
        print("End Process")
        break