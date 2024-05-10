#include <graphics.h>
#include <stdlib.h>
#include <stdio.h>
#include <conio.h>
#include <dos.h>
void main()
{
   int i, j, offset;
   int gd = DETECT, gm;
   int xmax, ymax;
   initgraph(&gd, &gm, "..//BGI");

   for (i = 0; i <= 640; i++)
   {
      i = i + 30;
      cleardevice();
      // track
      setcolor(LIGHTGRAY);
      line(0, 450, 640, 450);
      line(0, 475, 640, 475);
      line(0, 480, 640, 480);

      for (j = 0; j < 3; j++)
      {
	 // 2nd coach
	 setfillstyle(INTERLEAVE_FILL, WHITE);
	 offset = j * -180;
	 setcolor(WHITE); // WHITE
	 rectangle(30 + i + offset, 340, 180 + i + offset, 350);
	 rectangle(40 + i + offset, 350, 170 + i + offset, 425);

	 floodfill(41 + i + offset, 351, WHITE);

	 // back wheels
	 setcolor(DARKGRAY);
	 circle(70 + i + offset, 437, 12);
	 circle(140 + i + offset, 437, 12);
	 // WHEel rim
	 setcolor(LIGHTGRAY);
	 circle(70 + i + offset, 437, 8);
	 circle(140 + i + offset, 437, 8);
	 rectangle(70 + i + offset, 435, 140 + i + offset, 439);

	 // back windows
	 setcolor(9);
	 setfillstyle(INTERLEAVE_FILL, 9);
	 rectangle(40 + i + offset, 365, 170 + i + offset, 400);
	 floodfill(41 + i + offset, 366, 9);
	 line(83 + i + offset, 365, 83 + i + offset, 400);
	 line(122 + i + offset, 365, 122 + i + offset, 400);

	 // joint
	 setcolor(8);
	 rectangle(170 + i + offset, 400, 220 + i + offset, 390);
      }

      // engine

      setcolor(WHITE);
      setfillstyle(INTERLEAVE_FILL, WHITE);
      // rectangle(200 + i, 320, 260 + i, 330);
      //  floodfill(201 + i, 321, WHITE);

      rectangle(210 + i, 330, 250 + i, 400);
      //  floodfill(211 + i, 331, WHITE);

      // rectangle(250 + i, 340, 345 + i, 425);
      line(330 + i, 340, 360 + i, 425);
      line(330 + i, 425, 360 + i, 425);

      rectangle(250 + i, 340, 330 + i, 425);
      floodfill(251 + i, 341, WHITE);

      //  front wheels
      setcolor(8);
      circle(225 + i, 425, 25);
      circle(320 + i, 437, 12);
      circle(280 + i, 437, 12);
      // front small incircle
      setcolor(7);
      circle(320 + i, 437, 8);
      circle(280 + i, 437, 8);
      rectangle(320 + i, 435, 280 + i, 439);
      // front big incircle
      setcolor(7);
      circle(225 + i, 425, 15);

      // front windows

      setfillstyle(INTERLEAVE_FILL, 9);
      setcolor(11);

      rectangle(220 + i, 335, 240 + i, 365);
      floodfill(221 + i, 336, 11);
      // light
      setcolor(12);
      rectangle(345 + i, 360, 355 + i, 380);

      // Chimney
      setcolor(WHITE);
      rectangle(300 + i, 300, 330 + i, 340);
      rectangle(290 + i, 290, 340 + i, 300);
      setcolor(DARKGRAY);
      setfillstyle(LTSLASH_FILL, DARKGRAY);
      circle(300 + i, 300 - i, 35);
      floodfill(300 + i, 300 - i, DARKGRAY);

      // hills
      setcolor(GREEN);
      line(0, 200, 50, 150);
      line(50, 150, 150, 200);
      line(150, 200, 300, 100);
      line(300, 100, 450, 175);
      line(450, 175, 640, 125);
      // sun
      setcolor(14);
      setfillstyle(SOLID_FILL, YELLOW);
      circle(475, 75, 25);
      floodfill(475, 75, YELLOW);
      delay(1000);
      getch();
   }
   getch();
   closegraph();
}
