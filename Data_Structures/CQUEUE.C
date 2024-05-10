#include <stdio.h>
#include <cstdlib>

#define capacity 6

int queue[capacity];
int front = -1, rear = -1;

int checkFull()
{
	if ((front == rear + 1) || (front == 0 && rear == capacity - 1))
	{
		return 1;
	}
	return 0;
}

int checkEmpty()
{
	if (front == -1)
	{
		return 1;
	}
	return 0;
}

void enqueue()
{
	int value;
	printf("Enter element to add\n");
	scanf("%d", &value);
	if (checkFull())
		printf("Overflow condition\n");

	else
	{
		if (front == -1)
			front = 0;

		rear = (rear + 1) % capacity;
		queue[rear] = value;
		printf("%d was enqueued to circular queue\n", value);
	}
}

int dequeue()
{
	int variable;
	if (checkEmpty())
	{
		printf("Underflow condition\n");
		return -1;
	}
	else
	{
		variable = queue[front];
		if (front == rear)
		{
			front = rear = -1;
		}
		else
		{
			front = (front + 1) % capacity;
		}
		printf("%d was dequeued from circular queue\n", variable);
		return 1;
	}
}

void display()
{
	int i;
	if (checkEmpty())
		printf("Nothing to dequeue\n");
	else
	{
		printf("\nThe queue looks like: \n");
		for (i = front; i != rear; i = (i + 1) % capacity)
		{
			printf("%d ", queue[i]);
		}
		printf("%d \n\n", queue[i]);
	}
}

int main()
{
	int choice = 1;
	while (choice != 0)
	{
		printf("\nEnter choice");
		printf("1:enqueue\t2:dequeue\t3:peek\n4Display\t0:exit\n");
		scanf("%d", &choice);
		switch (choice)
		{
		case 1:
			enqueue();
			display();
			break;
		case 2:
			dequeue();
			display();
			break;
		case 3:
			// peek();
			break;
		case 4:
			display();
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
