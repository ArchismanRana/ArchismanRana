print("Multiplication Table by Python")

while True:
    print("Choices:")
    print("1: Get table of any one natural number at a time.\n"
          "2: Get tables of a group of natural numbers at a time.\n"
          "3: Exit")
    x = int(input("Make a choice:"))
    if x == 1:
        while True:
            A = int(input("Enter the no. whose multiplication table u want = "))
            for i in range(1, 11):
                print(A, "x", i, "=", A * i)

            Repeat_Process = input('Do you want multiplication table for another no. (Yes/No): ')
            if Repeat_Process == "Yes" or Repeat_Process == "yes":
                continue
            else:
                print("End Process")
                break

    elif x == 2:
        v = int(input("Enter the number upto which you want the tables:"))
        for w in range(1, v + 1):
            for t in range(1, 11):
                c = w * t
                print(w, 'x', t, '=', c)
            print(" ")
        print()

    elif x == 3:
        print("End Process.....Thank You!!")
        break

    else:
        print("Enter your choice as [1,2,3]")
        continue
