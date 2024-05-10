#include <stdio.h>
#include <math.h>
#include <conio.h>
#include <graphics.h>

int x1 = 30, x2 = 20, x3 = 40, y1 = 20, y2 = 40, y3 = 40;
int tx, ty;
void triangle(int x1, int y1, int x2, int y2, int x3, int y3)
{
	line(x1 + 320, y1 + 240, x2 + 320, y2 + 240);
	line(x2 + 320, y2 + 240, x3 + 320, y3 + 240);
	line(x1 + 320, y1 + 240, x3 + 320, y3 + 240);
}

void scale(int x1, int y1, int x2, int y2, int x3, int y3, int sx, int sy)
{
	x1 = x1 * sx;
	y1 = y1 * sy;
	x2 = x2 * sx;
	y2 = y2 * sy;
	x3 = x3 * sx;
	y3 = y3 * sy;
	triangle(x1, y1, x2, y2, x3, y3);
}

void rotate(int x1, int y1, int x2, int y2, int x3, int y3, float a)
{
	int xx1, xx2, xx3, yy1, yy2, yy3, c, s;
	a = a * 3.14 / 180;
	c = cos(a);
	s = sin(a);
	x1 = x1;
	x2 = x2;
	x3 = x3;
	xx1 = abs(x1 * c - y1 * s);
	yy1 = abs(y1 * c + x1 * s);
	xx2 = abs(x2 * c - y2 * s);
	yy2 = abs(y2 * c + x2 * s);
	xx3 = abs(x3 * c - y3 * s);
	yy3 = abs(y3 * c + x3 * s);
	//printf("%d %d %d %d %d %d", xx1, yy1, xx2, yy2, xx3, yy3);
	triangle(xx1, yy1, xx2, yy2, xx3, yy3);
}

void translate()
{
	printf("Enter X translation ");
	scanf("%d", &tx);
	printf("Enter Y translation ");
	scanf("%d", &ty);

	triangle(x1 + tx, y1 + ty, x2 + tx, y2 + ty, x3 + tx, y3 + ty);
}


void reflect()
{
	int rx,ry;
	printf("Along X axis (0/1) ");
	scanf("%d", &rx);
	printf("Along Y axis (0/1) ");
	scanf("%d", &ry);

	triangle(x1+(rx* 2* -x1), y1 +(ry * 2 * -y1), x2 +(rx* 2* -x2), y2 + (ry * 2 * -y2), x3 +(rx* 2* -x3), y3 +(ry * 2 * -y3));
}

void main()
{
	int gd = DETECT, gm;
	int sx, sy, tx, ty, opt;
	float a;
	// int x1=30+320,x2=20+320,x3=40+320,y1=20,y2=40,y3=40;
	initgraph(&gd, &gm, "..//BGI");
	triangle(x1, y1, x2, y2, x3, y3);

	while (opt != 0)
	{
		printf("Enter operation\n0:exit\n1:translation\n2:scaling\n3:rotation\n4:Reflection\n ");
		printf("Enter option ");
		scanf("%d", &opt);
		switch (opt)
		{
		case 1:
		{ // translation
			/*	printf("%d",getmaxx());
		printf("%d",getmaxy()); */
			translate();
			break;
		}

		case 2:
		{ // scaling
			printf("Enter X scale ");
			scanf("%d", &sx);
			printf("Enter Y scale ");
			scanf("%d", &sy);

			scale(x1, y1, x2, y2, x3, y3, sx, sy);
			break;
		}
		case 3:
		{
			// rotation
			printf("Enter rotation angle ");
			scanf("%d", &a);
			rotate(x1, y1, x2, y2, x3, y3, a);
		}
		case 4:
		{
		      reflect();
		}
		}
	}
	getch();
	closegraph();
}