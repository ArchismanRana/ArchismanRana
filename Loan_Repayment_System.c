#include<stdio.h>
int main()
{
    float repay , principle , time ,simple_intrest , rate;
    printf("Enter the principle amount , time(in years) :\n");
    scanf("%f%f",&principle,&time);
    if(principle<=100000)
    {
        rate = 10;
    }
    else if ((principle>100000)&&(principle<=500000))
    {
        rate = 8;
    }
    else
    {
        rate = 6;
    }
    simple_intrest = (principle*time*rate)/100;
    repay = simple_intrest + principle;
    printf("\nTotal Amount to be paid including intrest %.2f is : %.2f",simple_intrest,repay);
    return 0;
}