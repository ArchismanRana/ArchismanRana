#include <stdio.h>

int main()
{
    int n;
    char choice;

    do
    {
        printf("Multiplication Table of any Natural Number\n");
        printf("Enter number: ");
        scanf("%d", &n);

        printf("\n");
        printf("\nMultiplication Table of %d:\n", n);
        for (int i = 1; i<= 10; ++i)
        {
            printf("%d x %d = %d\n", n, i, n * i);
        }

        // Prompt user for another table
        printf("\nWant another table? (Y/N): ");
        scanf(" %c", &choice); // Notice the space before %c to consume any leftover newline character
    } while (choice == 'Y' || choice == 'y');
    
    return 0;
}