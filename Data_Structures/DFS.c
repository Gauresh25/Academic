#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

#define max 10
int stack[max];
int top = -1;

int visited[7] = {0, 0, 0, 0, 0, 0, 0};
int graph[7][7] = {
    {0, 1, 1, 1, 0, 0, 0},
    {1, 0, 1, 0, 0, 0, 0},
    {1, 1, 0, 1, 1, 0, 0},
    {1, 0, 1, 0, 1, 0, 0},
    {0, 0, 1, 1, 0, 1, 1},
    {0, 0, 0, 0, 1, 0, 0},
    {0, 0, 0, 0, 1, 0, 0}};

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
        printf("Underflow");
    }
    else
    {
        return (top--);
    }
}
void DFS(int init)
{
    int i, j;
    printf("%d ", init);
    visited[init] = 1;
    push(init);
    while (top != -1)
    {
        int node = pop();
        for (int j = 0; j < 7; j++)
        {
            if (graph[node][j] == 1 && visited[j] == 0)
            {
                printf("%d ", j);
                visited[j] = 1;
                push(j);
            }
        }
    }
}

int main()
{
    int val;
    printf("Enter beginning element:\n");
    scanf("%d", &val);
    DFS(val);

    getch();
    return 0;
}
