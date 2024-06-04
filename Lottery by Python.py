import random

n = random.randint(1, 6) #<-- You can put any integer number in place of 6
print("Lottery By Python!!!")
while True:
    guess = int(input("Guess the number between 1 to 6 :"))
    if n == guess:
        print("Congratulations, You won the lottery ")
        break
    else:
        print("Sorry, Try again, The lucky number was : ", n)
        continue
