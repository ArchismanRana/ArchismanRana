#include <stdio.h>
#include <math.h>
#define PI 3.14

int main(){
    int i, degree;
    float nume, deno, x, sum=0, term;
    printf("Enter the angle in degree:");
    scanf("%d", &degree);
    x=degree*(PI/180);
    nume=x;
    deno=1;
    i=2;
    do
    {
        term = nume/deno;
        nume = -nume*x*x;
        deno = deno*i*(i+1);
        sum = sum + term;
        i=i+2;
    } while (fabs(term)>=0.00001);
    printf("The sine of %d is %.3f\n", degree, sum);
    printf("The sine of %d using library function is %.3f\n", degree, sin(x));
    return 0;
}