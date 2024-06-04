import mysql.connector as q
import random


def Instructions():
    print("Welcome to Kaun Banega Crorepati!")
    print("\nInstructions:")
    print("1. You will be asked a series of questions, each with four options: A, B, C, and D.")
    print("2. Each correct answer will earn you money, increasing with each level.")
    print("3. You can win up to Rs. 10,000,000 if you answer all questions correctly.")
    print("4. To answer a question, type the letter corresponding to your chosen option (A, B, C, or D) and press Enter.")
    print("5. If you answer a question incorrectly, the game will end, and you will lose the chance to win further money.")
    print("6. You can choose to quit the game at any time by typing 'quit'.")
    print("\nLet's start the game!\n")


def Game():
    Money = 0
    levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 500000, 750000, 1000000]
    level_index = 0

    while True:
        Con = q.connect(host='localhost', user='root', password='qwerty')
        if Con.is_connected():
            cursor = Con.cursor()
            cursor.execute("USE KBC_QBank")
            cursor.execute("SELECT * FROM KBC_Q")
            questions = cursor.fetchall()
            Con.close()

            if level_index >= len(levels):
                print("Congratulations! You've completed all levels!")
                break

            random_Q_index = random.randint(0, len(questions) - 1)
            question_data = questions[random_Q_index]

            Question = question_data[1]
            O_A = question_data[2]
            O_B = question_data[3]
            O_C = question_data[4]
            O_D = question_data[5]
            Ans = question_data[6]

            print(f"Question for Rs. {levels[level_index]}")
            print(Question)
            print(f"A. {O_A}")
            print(f"B. {O_B}")
            print(f"C. {O_C}")
            print(f"D. {O_D}")

            user = input("Enter your answer (A/B/C/D): ").strip().upper()

            if user == Ans:
                Money += levels[level_index]
                level_index += 1
                print(f"Congratulations!! You win Rs. {levels[level_index - 1]}")
                print(f"The correct answer is: {Ans}")
                continue
            else:
                print("Wrong Answer....Better luck next time!")
                print(f"The correct answer is: {Ans}")
                break


while True:
    print("Welcome to Kaun Banega Crorepati!")
    print("1. Start Game")
    print("2. Instructions")
    print("3. Exit")
    choice = int(input("Choose an option: "))
    if choice == 1:
        Game()
    elif choice == 2:
        Instructions()
        continue
    elif choice == 3:
        print("Thank You!!!......")
        break
    else:
        print("Enter correct No.")
        continue
