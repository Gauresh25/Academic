#include<graphics.h>
#include<math.h>

void draw(int x1,int y1,int x2,int y2);
void main()
{
	int gd = DETECT,gm;
	int x1=0,y1=0,x2=0,y2=0;
	initgraph(&gd,&gm,"..//BGI");
	printf("Enter first point \n");
	scanf("%d%d",&x1,&y1);
	printf("Enter second point \n");
	scanf("%d%d",&x2,&y2);
	draw(x1,y1,x2,y2);
	getch();
	closegraph();
}

void draw(int x1,int y1,int x2,int y2)
{
	int i,x,y,dx,dy,p,s1,s2,temp,swap=0;
	dx=abs( x2 - x1);
	dy=abs( y2 - y1);
	if(x2-x1<0)
	{	s1=-1;   }
	else if(x2-x1>0)
	{	s1=1;   }
	else
	{	s1=0;}

	if(y2-y1<0)
	{	s2=-1;   }
	else if(y2-y1>0)
	{	s2=1;   }
	else
	{	s2=0;}
	if (dy>dx)
	{
		temp = dy;
		dy = dx;
		dx = temp;
		swap=1;
	}
	x=x1;
	y=y1;
	p= 2*dy - dx;
	for(i=0;i<dx;i++)
	{
		if(p<0)
		{
			if(swap==1)
			{
				x=x+s1;
			}
			else
			{

				y=y+s2;
			}
			p=p+2*dy;
		}
		else
		{
			x=x+s1;
			y=y+s2;
			p=p + 2*dy - 2*dx;
		}
		putpixel(x,y,WHITE);
		delay(10);
	}
}