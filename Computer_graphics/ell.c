#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <graphics.h>
void main()
{
    int gd = DETECT, gm;
    int rx, ry, i, j, x, y, xi, yi;
    float p1, p2;
    initgraph(&gd, &gm, "C:\\TURBOC3\\BGI");
    printf("Enter rx and ry : ");
    scanf("%d%d", &rx, &ry);
    x = 0;
    xi = 0;
    y = ry;
    yi = 0;

    p1 = ry ^ 2 - rx ^ 2 * ry + 1 / 4 * (rx ^ 2);
    while (2 * (ry ^ 2) * x <= 2 * (rx ^ 2) * y)
    {
        if (p1 < 0)
        {
            x++;
            p1 = p1 + 2.0 * (ry ^ 2) * x + (ry ^ 2);
        }
        else
        {
            x++;
            y--;
            p1 = p1 + 2.0 * (ry ^ 2) * x - 2.0 * (rx ^ 2) * y + (ry ^ 2);
        }
        putpixel(320 + x, 240 + y, 15);
        putpixel(320 + x, 240 - y, 15);
        putpixel(320 - x, 240 + y, 15);
        putpixel(320 - x, 240 - y, 15);
    }
    p2 = (ry ^ 2) * (xi + 0.5) * (xi + 0.5) + (rx ^ 2) * (yi - 1) * (yi - 1) - (rx ^ 2) * (ry ^ 2);
    do
    {
        if (p2 > 0)
        {
            y--;
            p2 = p2 - 2 * (rx ^ 2) * y + (rx ^ 2);
        }
        else
        {
            x++;
            y--;
            p2 = p2 + 2 * (ry ^ 2) * x - 2 * (rx ^ 2) * y + (rx ^ 2);
        }
        putpixel(320 + x, 240 + y, 15);
        putpixel(320 + x, 240 - y, 15);
        putpixel(320 - x, 240 + y, 15);
        putpixel(320 - x, 240 - y, 15);
    } while (y >= 0);
    getch();
    closegraph();
}
