#include <stdio.h>
#include <stdbool.h>
#include <conio.h>
#include <stdlib.h>

int top = -1, max = 25;
char stack[25];
char infix[25];
char postfix[25];

void push(char item);
char pop();
int precedence(char o);
void convert();

int main()
{
	printf("Enter infix expression\n");
	fgets(infix, 25, stdin);

	printf("Infix expression is: %s\n", infix);
	convert();
	printf("Postfix expression is: %s\n", postfix);
	getch();
	return 0;
}

void convert()
{
	int i = 0, j = 0;
	for (i = 0; infix[i] != '\0'; i++)
	{
		if ((infix[i] >= 'a' && infix[i] <= 'z') || (infix[i] >= 'A' && infix[i] <= 'Z') || (infix[i] >= '0' && infix[i] <= '9'))
		{
			postfix[j++] = infix[i];
		}

		else if (infix[i] == '+' || infix[i] == '-' || infix[i] == '*' || infix[i] == '/' || infix[i] == '^')
		{
			while (top > -1 && precedence(stack[top]) >= precedence(infix[i]))
			{
				postfix[j++] = pop();
			}
			stack[++top] = infix[i];
		}

		else if (infix[i] == '(')
		{
			push(infix[i]);
		}
		else if (infix[i] == ')')
		{

			while (stack[top] != '(') //(a+b)*(c+d)
			{
				postfix[j++] = pop();
				if (stack[top] == '(')
				{
					pop();
					continue;
				}
			}
		}
		else
		{
			continue;
		}
	}
	while (top != -1)
	{
		postfix[j++] = pop();
	}
}

int precedence(char o)
{
	if (o == '^')
	{
		return 3;
	}
	if (o == '*' || o == '/')
	{
		return 2;
	}
	if (o == '+' || o == '-')
	{
		return 1;
	}
	else
	{
		return -1;
	}
}

void push(char item)
{
	if (top >= max)
	{
		printf("The stack is full\n");
		exit(0);
	}
	else
	{
		stack[++top] = item;
	}
}

char pop()
{
	if (top == -1)
	{
		printf("The stack is empty\n");
		exit(0);
	}
	return stack[top--];
}
