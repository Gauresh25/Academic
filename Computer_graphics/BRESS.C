#include<graphics.h>
#include<math.h>

#define sign(x) ((x>0)?1:((x<0)?-1:0))
void bres_general(int x1, int y1, int x2, int y2);
void main()
{
	int gd = DETECT,gm;
	int x1=0,y1=0,x2=0,y2=0;
	initgraph(&gd,&gm,"..//BGI");
	printf("Enter first point \n");
	scanf("%d%d",&x1,&y1);
	printf("Enter second point \n");
	scanf("%d%d",&x2,&y2);
	bres_general(x1,y1,x2,y2);
	getch();
	closegraph();
}

void bres_general(int x1, int y1, int x2, int y2)
{
  int dx, dy, x, y, d, s1, s2, swap=0, temp,i;

  dx = abs(x2 - x1);
  dy = abs(y2 - y1);
  s1 = sign(x2-x1);
  s2 = sign(y2-y1);

  /* Check if dx or dy has a greater range */
  /* if dy has a greater range than dx swap dx and dy */
  if(dy > dx){temp = dx; dx = dy; dy = temp; swap = 1;}

  /* Set the initial decision parameter and the initial point */
  d = 2 * dy - dx;
  x = x1;
  y = y1;

  for(i = 1; i <= dx; i++)
  {
    putpixel(x,y,WHITE);

    while(d >= 0)
    {
      if(swap) x = x + s1;
      else
      {
	y = y + s2;
	d = d - 2* dx;
      }
    }
    if(swap) y = y + s2;
    else x = x + s1;
    d = d + 2 * dy;
  }
}