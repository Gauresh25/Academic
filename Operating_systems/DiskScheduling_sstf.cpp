#include <iostream>
#include <conio.h>
#include <cmath>

using namespace std;
int n =10;
int head,curpos,seek=0;
class loc
{
	public:
	int req;
	bool vis =false;
}refer[5],temp;

int findMin(int head)
{
	int min_dist = 999;
	int nextReq = -1;
	int i;
	for(i = 0;i<5;i++)
	{
		if(!refer[i].vis&& abs(head - refer[i].req)<min_dist)
		{
			min_dist=abs(head - refer[i].req);
			nextReq= i;
		}
	}
	return nextReq;
}
int main()
{
	refer[0].req= 150;
	refer[1].req=10;
	refer[2].req=200;
	refer[3].req=80;
	refer[4].req=190;
	
	head = 50;
	for(int i = 0;i<5;i++)
	{
		curpos = findMin(head);
		refer[curpos].vis = true;
		seek += abs(refer[curpos].req - head);
		head =  refer[curpos].req;
		cout<<"visited "<<head<<endl;
	}
	int a =1024;
	cout<<log2(1024);
	return 0;}
