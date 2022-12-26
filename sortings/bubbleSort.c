#include<stdio.h>
#include<conio.h>
void main()
{
    int i,j,n,A[50];
    printf("Enter Array size");
    scanf(" %d ", &n);
    printf("Enter Array elements");
    for (i=0; i<n; i++)
    {
        scanf(" %d ", &A[i]); // entering the array elements
    }
    for (i=0; i<n; i++)     // no of steps
    {
        for (j=0; j < n-i-1; j++)
        {
            if (A[j] > A[j+1])
            {
                temp = A[j];
                A[j] = A[j+1];
                A[j+1] = temp;
            } 
        }
    }   
    printf("THE SORTED ARRAY IS :");
    for (i=0;i<n;i++)
    {
        printf(" %d ", &A[i])
    }
}