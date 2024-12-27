#include <stdio.h>

float c2f(float);

float c2f(float c){
    return (9*c)/5.0 + 32;
}

int main()
{
    float celcius;
    printf("Celcius To Farenheit\n");
    printf("Enter Temp (C):");
    scanf("%f", &celcius);
    printf("\n%.3f degree Celcius --> %.2f F", celcius, c2f(celcius));
    return 0;
}