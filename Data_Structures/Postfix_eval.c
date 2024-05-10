#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#define max 10
int stack[max];
int top = -1;

char postfix[20] = "523*+";

void push(int val)
{
    if (top != max)
    {
        stack[++top] = val;
    }
    else
    {

        printf("Overflow");
    }
}
int pop()
{
    if (top == -1)
    {
        // printf("Underflow");
    }
    else
    {
        return (stack[top--]);
    }
}
int evaluatePostfix()
{

    int i, val1, val2, j;

    for (i = 0; postfix[i] != '\0'; i++)
    {

        if (postfix[i] >= '0' && postfix[i] <= '9')
            push(postfix[i] - '0');

        else if (postfix[i] == '+' || postfix[i] == '*')
        {
            int val1 = pop();
            int val2 = pop();
            switch (postfix[i])
            {
            case '+':
                push(val2 + val1);
                break;
            case '-':
                push(val2 - val1);
                break;
            case '*':
                push(val2 * val1);
                break;
            case '/':
                push(val2 / val1);
                break;
            }
        }
    }
    return pop();
}
void main()
{
    printf("Orignal expression: %s \n", postfix);
    printf("Output: %d", evaluatePostfix());
    getch();
}