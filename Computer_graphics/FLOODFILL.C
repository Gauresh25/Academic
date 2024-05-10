#include <stdio.h>
#include <graphics.h>
struct stack
{
	int x;
	int y;
} st[10000];
void BoundaryFill(int x, int y, int bound, int col);
void push(int x, int y);
struct stack pop();
int t = -1;
void main()
{
	int col, gd = DETECT, gm;
	initgraph(&gd, &gm, "..\\boundI");
	rectangle(150, 150, 250, 250);
	// BoundaryFill(151, 151, 15);
	printf("Enter the value of colour: ");
	scanf("%d", &col);
	BoundaryFill(151, 151, 15, col);
	getch();
	closegraph();
}
void push(int x, int y)
{
	t++;
	st[t].x = x;
	st[t].y = y;
}
struct stack pop()
{
	struct stack p;
	p.x = st[t].x;
	p.y = st[t].y;
	t--;
	return p;
}
void BoundaryFill(int x, int y, int bound, int fill)
{
	struct stack temp;
	int color;
	push(x, y);
	while (t != -1)
	{
		temp = pop();
		color = getpixel(temp.x, temp.y);
		if (color != bound)
			putpixel(temp.x, temp.y, fill);
		x = temp.x;
		y = temp.y;
		color = getpixel(x + 1, y);
		if (color != fill && color != bound)
			push(x + 1, y);
		color = getpixel(x, y + 1);
		if (color != fill && color != bound)
			push(x, y + 1);
		color = getpixel(x - 1, y);
		if (color != fill && color != bound)
			push(x - 1, y);
		color = getpixel(x, y - 1);
		if (color != fill && color != bound)
			push(x, y - 1);
	}
}