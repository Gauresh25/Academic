#include <graphics.h>
#include <math.h>

void main()
{
	int gd = DETECT, gm;
	int i = 0;
	int x, y, dx, dy, xi, yi, x1, x2, y1, y2, m, steps, xm = getmaxx() / 2, ym = getmaxy() / 2;
	initgraph(&gd, &gm, "..//BGI");
	line(getmaxx() / 2, 0, getmaxx() / 2, getmaxy());
	line(0, getmaxy() / 2, getmaxx(), getmaxy() / 2);
	/*printf("Enter point 1\n");
	scanf("%d",&x1);
	scanf("%d",&y1);
	printf("Enter point 2\n");
	scanf("%d",&x2);
	scanf("%d",&y2);

	*/
	x1 = 20;
	y1 = 50;
	x2 = 300;
	y2 = 50;

	dx = x2 - x1;
	dy = y2 - y1;
	m = dy / dx;

	if (dy > dx)
	{
		steps = dy;
	}
	else
	{
		steps = dx;
	}

	x = x1;
	y = y1;
	if (m == 1)
	{
		xi = 1;
		yi = 1;
	}
	else
	{
		xi = abs(dx / steps);
		yi = abs(dy / steps);
	}
	xm = getmaxx() / 2;
	ym = getmaxy() / 2;
	for (i = 0; i < steps; i++)
	{

		x = floor(x + xi);
		y = floor(y + yi);

		// straigt line

		putpixel(x, y, WHITE);

		// dotted

		if (x % 2 != 0)
		{
			putpixel(x, y + ym, WHITE);
		}

		// dashed line

		if (x % 5 != 0)
		{
			putpixel(x + xm, y + ym, WHITE);
		}

		// thickline

		putpixel(x + xm, y, WHITE);
		putpixel(x + 1 + xm, y, WHITE);
		putpixel(x + xm, y + 1, WHITE);
		putpixel(x - 1 + xm, y, WHITE);

		delay(10);
	}
	getch();
	closegraph();
}