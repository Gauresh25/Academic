#include <graphics.h>
#include <math.h>

void drawTriangle(int x[], int y[]) {
    // Function to draw a triangle
    drawpoly(3, x);
}

void translate(int x[], int y[], int tx, int ty) {
    // Function to perform translation
    for (int i = 0; i < 3; i++) {
        x[i] += tx;
        y[i] += ty;
    }
}

void rotate(int x[], int y[], float angle) {
    // Function to perform rotation
    float radian = angle * (M_PI / 180.0);
    int ox = 0, oy = 0; // Origin at center of screen

    for (int i = 0; i < 3; i++) {
        int px = x[i] - ox;
        int py = y[i] - oy;
        x[i] = ox + (int)(px * cos(radian) - py * sin(radian));
        y[i] = oy + (int)(px * sin(radian) + py * cos(radian));
    }
}

void scale(int x[], int y[], float sx, float sy) {
    // Function to perform scaling
    int ox = 0, oy = 0; // Origin at center of screen

    for (int i = 0; i < 3; i++) {
        x[i] = ox + (int)(x[i] * sx);
        y[i] = oy + (int)(y[i] * sy);
    }
}

void reflect(int x[], int y[]) {
    // Function to perform reflection
    for (int i = 0; i < 3; i++) {
        x[i] = -x[i];
    }
}

void shear(int x[], int y[], float shx, float shy) {
    // Function to perform shear
    for (int i = 0; i < 3; i++) {
        x[i] = x[i] + shx * y[i];
        y[i] = y[i] + shy * x[i];
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    int x[] = {100, 200, 300}; // Initial x-coordinates of the triangle vertices
    int y[] = {100, 200, 100}; // Initial y-coordinates of the triangle vertices

    // Original triangle
    drawTriangle(x, y);

    // Translation
    translate(x, y, 50, 50);
    setcolor(RED);
    drawTriangle(x, y);

    // Rotation
    rotate(x, y, 45);
    setcolor(GREEN);
    drawTriangle(x, y);

    // Scaling
    scale(x, y, 1.5, 1.5);
    setcolor(BLUE);
    drawTriangle(x, y);

    // Reflection
    reflect(x, y);
    setcolor(YELLOW);
    drawTriangle(x, y);

    // Shear
    shear(x, y, 0.5, 0);
    setcolor(MAGENTA);
    drawTriangle(x, y);

    getch();
    closegraph();
    return 0;
}
