#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *next;
};
struct node *start = NULL, *last;

void Display()
{
    struct node *temp;
    if (start == NULL)
        printf("\nList is empty\n");
    else
    {
        printf("Linked list is : \n");
        temp = start;
        while (temp != NULL)
        {
            printf("%d\n", temp->data);
            temp = temp->next;
        }
    }
}
void Insert_front()
{
    int data;
    struct node *temp;
    temp = (struct node *)malloc(sizeof(struct node));
    printf("\nEnter data : ");
    scanf("%d", &data);
    temp->data = data;
    temp->next = start;
    start = temp;
}
void Insert_end()
{
    int data;
    struct node *temp, *p;
    temp = (struct node *)malloc(sizeof(struct node));

    printf("\nEnter data : ");
    scanf("%d", &data);

    temp->next = NULL;
    temp->data = data;
    p = start;
    while (p->next != NULL)
    {
        p = p->next;
    }
    p->next = temp;
}
void Insert_between()
{
    Display();
    struct node *p, *temp;
    int val, data;
    temp = (struct node *)malloc(sizeof(struct node));

    printf("\nEnter element after which data needs to be added :");
    scanf("%d", &val);
    printf("\nEnter data :");
    scanf("%d", &data);

    p = start;
    temp->data = data;
    temp->next = 0;
    while (p->data != val)
    {
        p = p->next;
    }
    temp->next = p->next;
    p->next = temp;
}
void Delete_first()
{
    struct node *temp;
    if (start == NULL)
        printf("\nList is empty\n");
    else
    {
        temp = start;
        start = start->next;
        temp->next = NULL;
        free(temp);
    }
}
void Delete_end()
{
    struct node *p, *q;
    if (start == NULL)
    {
        printf("\nList is Empty\n");
    }
    p = start;
    while (p->next->next != NULL)
    {
        p = p->next; // p has 2nd last node
    }
    q = p->next;
    free(q);
    p->next = NULL;
}
void Delete_between()
{
    struct node *p, *q;
    int val;
    Display();
    if (start == NULL)
        printf("\nList is empty\n");
    else
    {
        printf("\nEnter node after which data will be deleted: ");
        scanf("%d", &val);
        p = start;
        while (p->next->data != val)
        {
            p = p->next;
        }
        q = p->next;
        p->next = q->next;
        q->next = NULL;
        free(q);
    }
}
int main()
{
    int choice;
    printf("\n\t1  To see list\n");
    printf("\t2  For insertion at beggining\n");
    printf("\t3  For insertion at end\n");
    printf("\t4  For insertion in between\n");
    printf("\t5  For deleting  first element\n");
    printf("\t6  For deletion of last element\n");
    printf("\t7  For deletion in between\n");
    printf("\t8  To exit\n");
    while (1)
    {
        printf("\nEnter Choice of operation :\n");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
            Display();
            break;
        case 2:
            Insert_front();
            break;
        case 3:
            Insert_end();
            break;
        case 4:
            Insert_between();
            break;
        case 5:
            Delete_first();
            break;
        case 6:
            Delete_end();
            break;
        case 7:
            Delete_between();
            break;
        case 8:
            exit(1);
            break;
        default:
            printf("Invalid ");
        }
    }
    return 0;
}