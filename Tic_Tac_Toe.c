#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int player, computer = rand() % 3;
    /*
    0 --> snake
    1 --> water
    2 --> gun
    */
    printf("Choose 0 for snake, 1 for water, 2 for gun\n");
    scanf("%d", &player);
    printf("%d\n", computer);

    if (player == 0 && computer == 0)
    {
        printf("It's a Draw!!\n");
    }
    else if (player == 0 && computer == 1)
    {
        printf("You win!!\n");
        
    }
    else if (player == 0 && computer == 2)
    {
        printf("You lose!!\n");
    }
    else if (player == 1 && computer == 0)
    {
        printf("You lose!!\n");
    }
    else if (player == 1 && computer == 1)
    {
        printf("It's a Draw!!\n");
    }
    else if (player == 1 && computer == 2)
    {
        printf("You win!!\n");
    }
    else if (player == 2 && computer == 0)
    {
        printf("You win!!\n");
    }
    else if (player == 2 && computer == 1)
    {
        printf("You lose!!\n");
    }
    else if (player == 2 && computer == 2)
    {
        printf("It's a Draw!!\n");
    }
    else {
        printf("Try Again!!\n");
        
    }
    return 0;
}