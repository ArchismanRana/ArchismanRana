import random
#A Coin is tossed
while True:
    x = random.choice(['Head','Tail'])
    print(x)
    if x == ("Head"):
        y = random.randint(1,6)
        print(y)

        if y in (2,4,6):
            y = random.randint(1,6)
            print(y)
        else:
            print()
    else:
        print()
    Repeat_Process = input("Do you want to start again (Yes/No): ")
    if Repeat_Process == "Yes" or Repeat_Process == "yes":
        continue
    else:
        print("Thank You!!")
        break
