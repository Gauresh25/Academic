#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

int max = 25;
int queue[25];
int front = -1, rear = -1;

void enqueue()
{
	int ele;
	if (rear == max - 1)
	{
		printf("Queue is full\n");
		return;
	}
	if (front == -1)
	{
		front++;
	}
	printf("Enter element to add\n");
	scanf("%d", &ele);
	queue[++rear] = ele;
}

void deque()
{
	int ele;
	if (front > rear)
	{
		printf("Queue is Empty\n");
		return;
	}
	ele = queue[front++];
	printf("Element dequed is %d", ele);
}

int peek()
{
	return (queue[front]);
}

void isFull()
{
	if (rear == max - 1)
	{
		printf("Queue is full");
	}
}
void isEmpty()
{
	if (front > rear)
	{
		printf("Queue is empty\n");
	}
}

void display()
{
	int i = 0;
	if (front > rear)
	{
		printf("Queue is empty\n");
		return;
	}
	printf("Queue:\n");
	for (i = front; i <= rear; i++)
	{
		printf("%d\t", queue[i]);
	}
}

int main()
{
	int choice = 1;
	printf("Enter max size of Queue");
	scanf("%d", &max);
	while (choice != 0)
	{
		printf("\nEnter choice");
		printf("1:enqueue\n2:dequeue\n3:peek\n4Display\n5Isfull\n6IsEmpty\n0:exit\n");
		scanf("%d", &choice);
		switch (choice)
		{
		case 1:
			enqueue();
			display();
			break;
		case 2:
			deque();
			display();
			break;
		case 3:
			peek();
			break;
		case 4:
			display();
			break;
		case 5:
			isFull();
			break;
		case 6:
			isEmpty();
			break;
		case 0:
			exit(0);
			break;
		default:
			printf("Invalid operation");
			break;
		}
	}
	return (0);
}
