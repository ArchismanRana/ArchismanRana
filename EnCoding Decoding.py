import random
import string

print("|| ENCODE AND DECODE YOUR CHATS ||")
while True:
    print("1] Code the chat")
    print("2] Decode the chat")
    print("3] Exit")
    x = int(input("Enter your choice:"))
    if x == 1:
        M = input("Enter your chat:")
        words = M.split()
        nwords = []
        for word in words:
            if len(word) >= 3:
                random_letter_1 = random.choice(string.ascii_uppercase)
                random_letter_2 = random.choice(string.ascii_uppercase)
                new_word = random_letter_1 + word[1:] + word[0] + random_letter_2
                nwords.append(new_word)
            else:
                nwords.append(word[::-1])

        print(" ".join(nwords))

    elif x == 2:  # Decoding
        M = input("Enter your chat:")
        words = M.split()
        nwords = []
        for word in words:
            if len(word) >= 3:
                new_word = word[1:-1]  # Remove 1st and last random letter
                new_word = new_word[-1] + new_word[:-1]
                nwords.append(new_word)
            else:
                nwords.append(word[::-1])

            print(" ".join(nwords))

    else:
        print("Thank You...")
        break
