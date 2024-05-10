#include<stdio.h>
#include<graphics.h>
#include<conio.h>


struct pixel{
  int x,y;
}rmax,rmin,seed;

struct pixel temp,t,b,r,l;


int size=10000;
struct pixel stack[10000];
int top=-1;

void push(struct pixel temp)
{
     if(top==size-1)
     {
	return;
     }
     else
     {
     stack[++top]=temp;
     }
     //printf("element pushed");
}

struct pixel pop()
{
	if(top == -1)
	{
		return;
	}
       //	printf("element popped");
       else{
		return stack[top--];
		}
}

int isEmpty()
{
	if(top == 0)
	{
		return 1;
	}
	else
	{
		return 0;
	}
}
// && temp.x<rmax.x && temp.x>rmin.x && temp.y<rmax.y && temp.y>rmin.y
void FloodFill(struct pixel seed,int color)
{

	//seed.x<rmax.x && seed.x>rmin.x
	if(getpixel(seed.x,seed.y)==0)
	{
		push(seed);
	}
	while(top != -1)
	{
		temp=pop();
		if(getpixel(temp.x,temp.y)!=15)
		{
			putpixel(temp.x,temp.y,color);
			t=b=r=l=temp;
			t.y++;
			b.y--;
			r.x++;
			l.x--;

			push(t);
			push(b);
			push(r);
			push(l);
		}
	}
}
void main(){
     int a;
     int gd=DETECT, gm;
     rmin.x=200;
rmin.y=200;
rmax.x=400;
rmax.y=400;

     seed.x = 300;
     seed.y = 300;


     initgraph(&gd,&gm,"..//BGI");

     rectangle(rmin.x,rmin.y,rmax.x,rmax.y);
     FloodFill(seed,BLUE);
     getch();
}
