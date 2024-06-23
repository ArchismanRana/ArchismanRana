import random

n = random.randint(1, 100)
a = -1
guesses = 1
while a != n:
    a = int(input("Guess the number:"))
    if a >= n + 5:
        print("Try some lower number...")
        guesses += 1
    elif a <= n - 5:
        print("Try some higher number...")
        guesses += 1
    elif n + 1 <= a <= n + 5:
        print("You are very close to the number. Try to go lower")
        guesses += 1
    elif n - 5 <= a <= n - 1:
        print("You are very close to number. Try to go higher")
        guesses += 1

print(f"You have guessed the number {n} correctly in {guesses} attempts")
