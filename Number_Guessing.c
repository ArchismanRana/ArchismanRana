#include <stdio.h>
#include <stdlib.h> // has rand() function
#include <time.h>

int main()
{
    printf("....GUESS THE NUMBER GAME....\n");
    // Initialize random no. generator
    srand(time(0));
    int randomNumb = (rand() % 100) + 1;
    int Guess, Score=100;
    int no_of_guesses = 0;
    // rand() gives random no. and (% 100) gives remainder which lies in 0 to 99 
    // printf("Random Number: %d\n", randomNumb);

    do
    {
        printf("Guess the number:");
        scanf("%d", &Guess);
        // Conditions
        if (Guess < randomNumb-5)
        {
            printf("You entered lower number. Try Again!\n");
            no_of_guesses += 1;
            Score -= 4;
        }
        else if (Guess > randomNumb+5)
        {
            printf("You entered higher number. Try Again!\n");
            no_of_guesses += 1;
            Score -= 4;
        }
        else if (Guess == randomNumb)
        {
            printf("Congratz!! You guessed it correctly\n");
            printf("Total Guesses: %d\n", no_of_guesses);
            printf("Your Score: %d/100", Score);
        }
        else if (Guess > randomNumb-5 && Guess < randomNumb)
        {
            printf("Close enough.... Try some higher no.\n");
            no_of_guesses += 1;
            Score -= 4;
        }
        else if (Guess < randomNumb+5 && Guess > randomNumb)
        {
            printf("Close enough.... Try some lower no.\n");
            no_of_guesses += 1;
            Score -= 4;
        }
        else if (Guess<1 || Guess>100)
        {
            printf("Guess the number between 1 to 100\n");
        }
        
        else
        {
            printf("Enter integer number\n");
        }
        
        
        
    } while (Guess!=randomNumb);
    
    return 0;
}