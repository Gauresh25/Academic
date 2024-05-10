#include<stdio.h>
#include<conio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *next;
};
void main(){
    int choice = 1;
    struct node *start=NULL,*temp,*last,*ptr;
    
    start =(struct node*)malloc(sizeof(struct node));
    printf("Enter first data element :");
    scanf("%d",&start->data);
    start->next=NULL;
    last = start;

    while(choice==1)
   {
    temp =(struct node*)malloc(sizeof(struct node));
    printf("Enter data:");
    scanf("%d",&temp->data);
    temp->next = NULL;
    last->next=temp;
    last = temp;
    printf("add more elements?(1/0)");
    scanf("%d",&choice);
    }

    printf("List elements are ");
    ptr = start;
    while(ptr != NULL) 
    {
    printf(" %d ",ptr->data);
    ptr = ptr->next;
    }
}