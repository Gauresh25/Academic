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
       /*putpixel(xm+y,ym+x,15);
	putpixel(xm+y,ym-x,15);
	putpixel(xm-y,ym+x,15);
	putpixel(xm-y,ym-x,15);*/

}
void drawEllipse(int rx,int ry)
{
	int x,y,p1,p2;
	x=0;                   //init values
	y=ry;
	p1=(ry^2)-(rx^2*ry)-(rx^2)/4;
	symPlot(x,y);

	while(2())   ////////
	{

		if(p1<0)
		{
			x=x+1;
			//y same
			p1=p1+(2*ry^2)*x+(ry^2);
		}
		else
		{
			x=x+1;
			y=y-1;
			p1=p1+(2*ry^2)*x-2(rx^2)*y+(ry^2);
		}
		symPlot(x,y);
		putpixel(x+320,y+240,15);
	}
}
void main()
{
	int x,y,p,steps,xin,yin,i,rx,ry,ring;
	int gd = DETECT,gm;
	initgraph(&gd,&gm,"..//BGI");

	printf("Enter radius x ");
	scanf("%d",&rx);
	printf("Enter radius y ");
	scanf("%d",&ry);
	drawEllipse(rx,ry);

	getch();
	closegraph();
}