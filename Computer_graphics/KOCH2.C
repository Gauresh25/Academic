
#include <math.h>
#include <graphics.h>

void koch(int it, int x1, int y1, int x5, int y5)
{
	int x2, y2, x3, y3, x4, y4;
	int dx, dy;
	if (it == 0)
	{
		line(x1, y1, x5, y5);
	}
	else
	{
		delay(10);
		dx = (x5 - x1) / 3;
		dy = (y5 - y1) / 3;
		x2 = x1 + dx;
		y2 = y1 + dy;
		x3 = (int)(0.5 * (x1 + x5) + sqrt(3) * (y1 - y5) / 6);
		y3 = (int)(0.5 * (y1 + y5) + sqrt(3) * (x5 - x1) / 6);
		x4 = 2 * dx + x1;
		y4 = 2 * dy + y1;
		koch(it - 1, x1, y1, x2, y2);
		koch(it - 1, x2, y2, x3, y3);
		koch(it - 1, x3, y3, x4, y4);
		koch(it - 1, x4, y4, x5, y5);
	}
}

int main()
{
	int it = 4;
	int gd = DETECT, gm;
	initgraph(&gd, &gm, "..//BGI");

	koch(it, 280, 280, 20, 280);
	getch();
	closegraph();
	return 0;
}