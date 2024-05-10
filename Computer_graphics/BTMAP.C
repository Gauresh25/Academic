#include <stdio.h>
#include <conio.h>
#include <graphics.h>
void main()
{
	int i, j, k, x, y;
	int gd = DETECT, gm;
	int G[7][5] = {{0, 1, 1, 1, 1},
				   {1, 0, 0, 0, 0},
				   {1, 0, 0, 0, 0},
				   {1, 0, 1, 1, 1},
				   {1, 0, 0, 0, 1},
				   {1, 0, 0, 0, 1},
				   {0, 1, 1, 1, 0}};

	initgraph(&gd, &gm, "..//BGI");
	for (k = 0; k < 7; k++)
	{
		for (i = 0; i < 5; i++)
		{
			putpixel(i + 100, k + 100, G[k][i] * 15);
		}
	}
	getch();
	closegraph();
}