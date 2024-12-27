#include <stdio.h>

// Reverse Array

void printArr(int arr[], int n){
    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]); 
    }
    printf("\n");  
}

// Swapping logic : Temp = a
//                   a = b
//                   b = Temp

void reverse(int arr[], int n){
    int temp;
    for (int i = 0; i < n/2; i++)
    {
        temp = arr[i];
        arr[i] = arr[n-i-1];
        arr[n-i-1]  = temp;

    }
    
}

int count(int arr[], int n){
    int no_of_positive=0;
    for (int i = 0; i < n; i++)
    {
        if (arr[i]>0){
            no_of_positive++;
        }
    }
    return no_of_positive;
}

int main()
{
    int arr[] = {1,3,-55,-322,6,21};
    printf("Original\n");
    printArr(arr, 6);
    reverse(arr, 6);
    printf("Reverse\n");
    printArr(arr, 6);
    printf("The no. of positive integers is %d\n", count(arr, 6));
    
    return 0;
}