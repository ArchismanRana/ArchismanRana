#include <stdio.h>
#include <string.h>
#include <ctype.h>

//void Caes_Ciph_En(char *text, int shift);
//void Pig_Latin_En(char *text);
//void caesarCipherDecode(char *text, int shift);
//void pigLatinDecode(char *text);

int main(){
    char text[200];
    int shift, choice;
    int run = 1;

    while (run)
    {
        printf("\nChoose an option:\n");
        printf("1. Encrypt message\n");
        printf("2. Decrypt message\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        switch (choice){
            case 1:
                printf("Enter the text:\n");
                fgets(text, sizeof(text), stdin);
                // printf("%s\n", text);
                printf("\nChoose an encoding method:\n");
                printf("1. Caesar Cipher\n");
                printf("2. Pig Latin\n");
                printf("Enter your choice: ");
                scanf("%d", &choice);

                if (choice == 1) {
                    printf("Enter the shift value: ");
                    scanf("%d", &shift);
                    //Caes_Ciph_En(text, shift);
                    strcat("CC:", text); 
                    printf("Encoded Text: %s\n", text);
                }
                
                else if (choice == 2){
                    //Pig_Latin_En(text);
                    strcat("PLAT:", text);
                    printf("Encoded Text: %s\n", text);   
                }

                else {
                    printf("Invalid choice!!\n");
                    return 1;
                }
                break;

        case 2:
            printf("\nChoose a decoding method:\n");
            printf("1. Caesar Cipher\n");
            printf("2. Pig Latin\n");
            printf("Enter your choice: ");
            scanf("%d", &choice);

            if (choice == 1) {
                //caesarCipherDecode(text, shift); // Shift is reused here
                printf("Decoded Text: %s\n", text);
            } else if (choice == 2) {
                //pigLatinDecode(text);
                printf("Decoded Text: %s\n", text);
            } else {
                printf("Invalid choice!\n");
            }
            break;

        default:
            printf("Invalid choice! Please try again.\n");
        }
    }
    return 0;
}