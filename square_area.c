#include <stdio.h>
#include <math.h>

int main()
{
    int a;
    printf("Enter length of side of square:");
    scanf("%d", &a);
    printf("Area of square: %f", pow(a, 2));
    return 0;
}