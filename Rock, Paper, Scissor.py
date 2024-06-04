import random


def comp_choice():
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    return computer


def user_choice():
    player = input("rock, paper or scissors?:").lower()
    while player not in ['rock', 'paper', 'scissors']:
        player = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return player


def det_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "Tie"
    elif (user_choice == "rock" and comp_choice == "scissors") or \
            (user_choice == "paper" and comp_choice == "rock") or \
            (user_choice == "scissors" and comp_choice == "paper"):
        return "Win"
    else:
        return "Lose"


def Game():
    p_score = 0
    c_score = 0
    while p_score < 100 or c_score < 100:
        u_ch = user_choice()
        c_ch = comp_choice()
        print(f"Computer chose:{c_ch}")
        result = det_winner(u_ch, c_ch)
        if result == "Win":
            p_score += 10
            print("You win this round!!")
        elif result == "Lose":
            c_score += 10
            print("You loose this round!!")
        else:
            print("It's a Tie!")

        print(f"Your current score : {p_score}")
        print(f"Computer current score : {c_score}")

        if p_score >= 100:
            print("Congratulations!! You got 100 points.")
            break
        elif c_score >= 100:
            print("Computer got 100 points. Better Luck next time")
            break

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break


def Instruction():
    print("Read Instructions carefully!!")
    print("1) Total Points 100")
    print("2) Both Player and Computer will get 10 points if they win the round.")
    print("3) If Tie than no one will get point")
    print("4) User must choose from rock, paper or scissors")


while True:
    print("Welcome to Rock, Paper, Scissor Game!!")
    print("1) Start the Game")
    print("2) Instructions")
    print("3) Restart")
    print("4) Exit")
    ch = int(input("Enter choice:"))
    if ch == 1:
        Game()
    elif ch == 2:
        Instruction()
        continue
    elif ch == 3:
        print("----RESTART----")
        Game()
    else:
        print("____Exiting Game____")
        break
