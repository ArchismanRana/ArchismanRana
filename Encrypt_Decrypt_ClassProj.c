#include <stdio.h>
#include <string.h>


void Encrypt(char str[]){
    for (int i = 0; i < strlen(str); i++)
    {
        str[i] = str[i] + 5;
        //printf("%c\n", str[i]);
    }
    printf("\nOutput: %s\n", str);
}

void Decrypt(char str[]){
    for (int i = 0; i < strlen(str); i++)
    {
        str[i] = str[i] - 5;
    }
    printf("\nOutput: %s\n", str);
}

int main(){
    char text[200];
    int shift; 
    char choice;
    int run = 1;

    while (run)
    {
        printf("\nChoose an option:\n");
        printf("1. Encrypt message\n");
        printf("2. Decrypt message\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        gets(choice);
        //getchar(); //To discard \n (newline char)

        switch (choice){
            case '1':
                printf("Enter the text:\n");
                gets(text);
                Encrypt(text);
                break;

            case '2':
                printf("Enter the Encoded text:\n");
                gets(text);
                Decrypt(text);
                break;
            
            case '3':
                printf("Exit Program\n");
                run=0;
                break;
            
            default:
                printf("Invalid choice. Try Again.\n");
            
        }
    }
    return 0;
}