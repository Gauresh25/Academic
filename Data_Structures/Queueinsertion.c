#include<stdio.h>       
#include<conio.h>

int Queue[100];
int front=-1,rear=0;
void insert()
{
    int val;
    printf("Enter element for queue");
    scanf("%d",&val);
    if (rear==99)
    {
        printf("invalid queue(overflow)");
        exit(0);
    }
    else
    {
    Queue[rear]=val;
    rear++;
    }
}
void main()
{
    int i;
    insert();
    insert();
    insert();
    insert();
    printf("the queue is: \n");
    for ( i = 0; i < rear; i++)
    {
        printf("%d\n",Queue[i]);
    }
}