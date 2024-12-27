#include <stdio.h>

int main()
{
    int income;
    float tax=0;
    printf("Enter income (per annum): \n");
    scanf("%d", &income);
    if (income<250000){
        tax = 0;
        printf("Tax applied: %0.3f",tax);
    }
    else if (income>250000 && income<500000){
        tax = 0.05* (income-250000);
        printf("Tax applied: %0.3f",tax);
    }
    else if (income>500000 && income<1000000){
        tax = 0.2* (income-500000);
        printf("Tax applied: %0.3f",tax);
    }
    else {
        tax = 0.3* (income-1000000);
        printf("Tax applied: %0.3f",tax);
    }
    return 0;
}