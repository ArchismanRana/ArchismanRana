def prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")


while True:
    print("Choices:")
    print("1: Check that number is prime or not.\n"
          "2: Generate prime numbers.\n"
          "3: Exit")
    x = int(input("Make a choice:"))

    if x == 1:
        while True:
            n = int(input("Enter a number:"))
            if n > 1:
                prime(n)
            else:
                print('Enter number greater than 1.')

            Repeat_Process = input("Do you want to check another number (Yes/No): ")
            if Repeat_Process == "Yes" or Repeat_Process == "yes":
                continue
            else:
                print("End Process")
                break

    elif x == 2:
        def prime_producer(end):
            for n in range(2, end):
                for h in range(2, n):
                    if n % h == 0:
                        break
                else:
                    print(n)


        v = int(input("Enter the last number upto which prime numbers will be generated:"))
        print(prime_producer(v))

    elif x == 3:
        print("End Process.....Thank You!!")
        break
