#include<stdio.h>
#include<math.h>
#include<conio.h>
#include<graphics.h>

void symPlot(int x,int y)
{
	int xm,ym;
	xm=320;
	ym=240;

	putpixel(xm+x,ym+y,15);
	putpixel(xm-x,ym+y,15);
	putpixel(xm+x,ym-y,15);
	putpixel(xm-x,ym-y,15);
	putpixel(xm+y,ym+x,15);
	putpixel(xm+y,ym-x,15);
	putpixel(xm-y,ym+x,15);
	putpixel(xm-y,ym-x,15);

}
void drawCircle(int r)
{
	int x,y,p;
	x=0;                   //init values
	y=r;
	p=1-r;
	symPlot(x,y);
	while(x<=y)
	{

		if(p<0)
		{
			x=x+1;
			//y same
			p=p+(2*x) +1;
		}
		else
		{
			x=x+1;
			y=y-1;
			p=p+(2*x)+1-(2*y);
		}
		symPlot(x,y);
		putpixel(x+320,y+240,15);
	}
}
void main()
{
	int x,y,p,steps,xin,yin,i,r,ring;
	int gd = DETECT,gm;
	initgraph(&gd,&gm,"..//BGI");

	printf("Enter radius ");
	scanf("%d",&r);
	printf("Enter rings ");
	scanf("%d",&ring);
	for(i=0;i<ring;i++)
	{
	//drawCircle(r);
	drawCircle(r+15*i);
	}
	getch();
	closegraph();
}
