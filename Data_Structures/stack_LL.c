#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
};

struct Node *head = NULL;

void push(int val)
{
    struct Node *newNode = malloc(sizeof(struct Node));
    newNode->data = val;

    newNode->next = head;

    head = newNode;
}

void pop()
{
    struct Node *temp;

    if (head == NULL)
        printf("Stack is Empty\n");
    else
    {
        printf("Popped element = %d\n", head->data);
        temp = head;
        head = head->next;
        free(temp);
    }
}

void display()
{
    struct Node *temp = head;

    while (temp != NULL)
    {
        printf("%d->", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

int main()
{
    int i, opt, choice;
    while (1)
    {
        printf("\nStack operations\n");
        printf("1 for insert\n2 for delete\n3  for display all elements of the queue\n0 for ending\n");
        printf("Enter option ");
        scanf("%d", &opt);
        switch (opt)
        {
        case 1:
            int val;
            printf("Enter value to be pushed ");
            scanf("%d", &val);
            push(val);
            break;
        case 2:
            pop();

            break;
        case 3:
            display();

            break;
        case 0:
            exit(1);
        }
    }
    return 0;
}