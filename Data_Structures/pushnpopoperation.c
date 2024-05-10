#include<stdio.h>       
#include<conio.h>
#include<stdlib.h>
#define max 10
int stack[max];
int top=-1;
void push()
{
    int val;
    printf("Enter value to be pushed ");
    scanf("%d",&val);
    if (top!=max)
    {
        stack[++top]=val;  
    }
    else
    {
        
        printf("Overflow");
    }
}
int pop()
{
    if (top==-1)
    {
        printf("Underflow");
    }
    else
    {
        return (top--);
    }
}
void main()
{
    int i,opt,choice;
    while(1)
    {
        printf("\nStack operations\n");
        printf("1 for insert\n2 for delete\n3 for peep\n4 for display all elements of the queue\n5 for ending\n");
        printf("Enter option ");
        scanf("%d",&opt);
        switch(opt)
        {
            case 1:
                push();
                break;
            case 2:
             pop();
                printf("\nelement deleted is %d\n",stack[top+1]);
                break;
            case 3:
                printf("\nelement at the top is %d\n",stack[top]);
                break;
            case 4:
                 printf("Stack: \n");
                for ( i = 0; i <= top; i++)
                {
                printf("%d\t",stack[i]);
                }
                break;
            case 5:
            exit(1);
        }
    }
}