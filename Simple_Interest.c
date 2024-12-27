#include <stdio.h>

int main()
{
    int p, t;
    float r = 8.23;
    float j;
    printf("Enter Principal amount: ");
    scanf("%d", &p);
    printf("Enter Time period: ");
    scanf("%d", &t);
    j = (p * r * t) / 100;
    printf("\nThe simple interest on amount of %d and time %d is: %f\n", p, t, j);
    return 0;
}
