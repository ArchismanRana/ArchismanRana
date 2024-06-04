# Roots of Quadratic eq. using Sridharacharya's Rule

while True:
    Quadratic_Eq = (input("Enter a Quadratic Eq. (ax^2 + bx + c = 0): "))
    a = int(input("Enter the value of a in ax^2 : "))
    b = int(input("Enter the value of b in bx : "))
    c = int(input("Enter the value of c in c : "))
    dis = b * b - 4 * a * c
    sqrt_val = dis ** 0.5

    # checking condition for discriminant
    if dis > 0:
        print(" real and different roots ")
        x = ((-b + sqrt_val) / (2 * a))
        y = ((-b - sqrt_val) / (2 * a))
        print("The roots of", Quadratic_Eq, "are", x, "and", y)
    elif dis == 0:
        print(" real and same roots")
        x = (-b / (2 * a))
        print("The roots of", Quadratic_Eq, "is", x)
        # when discriminant is less than 0
    else:
        print("Complex Roots")
        x = ((- b + sqrt_val) / (2 * a))
        y = ((- b - sqrt_val) / (2 * a))
        print("The roots of", Quadratic_Eq, "is", x, y)

    
    Repeat_Process = input("Do u want to repeat the process(Yes/No):")
    if Repeat_Process == "Yes" or Repeat_Process == "yes":
        continue
    elif Repeat_Process == "No" or Repeat_Process == "no":
        print("End Process")
        break
    else:
        break
        
