#include<stdio.h>
#include<conio.h>
#include<dos.h>
#include<graphics.h>
int i;
int speed()
{return i+1;  }
void jump(int j,int i)
{
	line(50+i,300-j,70+i,300-j);
 arc(85+i,300-j,0,180,15);
 line(100+i,300-j,140+i,300-j);
 arc(155+i,300-j,0,180,15);
 line(170+i,300-j,190+i,300-j);
 line(190+i,300-j,190+i,275-j);
 line(190+i,275-j,157+i,270-j);
 line(157+i,270-j,120+i,255-j);
 //line(145,25,0,80,250);
 //line(145,250,190,280);
 line(120+i,255-j,80+i,255-j);
 line(80+i,255-j,50+i,270-j);
 line(50+i,270-j,50+i,300-j);
 //car window
 line(126+i,263-j,152+i,276-j);
 line(152+i,276-j,110+i,272-j);
 line(110+i,272-j,110+i,263-j);
 line(110+i,263-j,126+i,263-j);
 line(105+i,272-j,105+i,263-j);
 line(105+i,263-j,80+i,263-j);
 line(80+i,263-j,70+i,272-j);
 line(70+i,272-j,105+i,272-j);
 //wheels
 circle(85+i,300-j,10);
 circle(155+i,300-j,10);
 circle(85+i,300-j,8);
 circle(155+i,300-j,8);
 line(85+i,292-j,85+i,300-j);
 line(76+i,297-j,85+i,300-j);
 line(79+i,309-j,85+i,300-j);
 line(95+i,298-j,85+i,300-j);
 line(92+i,310-j,85+i,300-j);

 line(155+i,302-j,155+i,290-j);
 line(147+i,296-j,155+i,300-j);
 line(149+i,309-j,155+i,300-j);
 line(164+i,298-j,155+i,300-j);
 line(163+i,309-j,155+i,300-j);
 //man
 circle(117+i,270-j,4);
 //color
 setfillstyle(1,RED);
 floodfill(55+i,280-j,WHITE);
 delay(10);
 cleardevice();
}
void move()
{
 int j=0 ;
 //moving car
 for(i=0;i<=369;i=speed())
 {
 outtextxy(110,150,"Welcome to moving Car Animation created by group(201_212)");
 //Car Body
 if(i<=200 || i>=300){
 jump(0,i);
 }else
      { if(i<=250){
       j=j+1;
       jump(j,i);

      }
      else{  j=j-1;
jump(j,i);
 }
 }
 //ROAD
 line(0,312,639,312);
 line(0,314,639,314);
 }



}
void main()
{
 int gd=DETECT,gm;
 initgraph(&gd,&gm,"c:\\turboc3\\bgi");

 move();

 getch();
}
