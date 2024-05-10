#include<stdio.h>
#include<conio.h>

#define Max 100
int queue[Max];
int rear=-1;
int front=-1;
/*insertion always at rear end, deleting done on front end*/
void insert(int element)
{
        if(rear==Max-1)
        {
                printf("\nQueue Overflow\n");
                return;
        }
        if( front == -1 )
        {
            front = 0;
        }
        rear++;
        queue[rear]=element ;
}

int del()
{
    int element;
    front=front+1;
    if( front>rear)
    {
        printf("\nQueue Underflow\n");
        exit(1);
    }
    element=queue[front-1];
    return element;
}

void show()
{
    int i;
    if ( front>rear)
    {
        printf("\nQueue is empty\n");
    }

    for(i=front;i<=rear;i++)
    {   
        printf("%d ",queue[i]);
    }
}

int main()
{
    int option,element,choice=1;
    
    printf("\navailable operations\n");
    printf("1 for insert\n2 for delete\n3 for display all elements of the queue\n4 for ending\n");
    do
    {
        printf("Enter option ");
        scanf("%d",&option);
        switch(option)
        {
            case 1:
                printf("\nelement to be added");
                scanf("%d",&element);
                insert(element);
                break;
            case 2:
                element=del();
                printf("\nelement deleted is %d\n",element);
                break;
            case 3:
                printf("\nQueue is :\n");
                show();
                break;
            case 4:
            exit(3);
        }

    }while(choice!=5);
return 0;
}