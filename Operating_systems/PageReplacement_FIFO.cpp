#include <iostream>
#include <conio.h>

using namespace std;
int queue[3];
int front = 0;
int rear = -1;

void enque(int val)
{
	int i=0;
	if (rear<3)
	{
		queue[++rear] = val;
	}
	else
	{
		for(i = 0;i<3-1;i++)
		{
			queue[i] = queue[i+1];
		}
		queue[i]=val;
	}
}

bool inQ(int x)
{
	for(int i =0;i<3;i++)
	{
		
		if(queue[i]==x)
			return true;
	}
	return false;
}



int main()
{
	int ref[10] ={7,0,1,2,0,3,0,4,2,3};
	//int frSize =3;
	for(int i =0;i<3;i++)
			queue[i] = -1;
	for(int i = 0;i<10;i++)
	{
		if(inQ(ref[i]))
			cout<<"page hit"<<endl;
		else
		{
			enque(ref[i]);
			cout<<"page miss"<<endl;
		}
		for(int i =0;i<3;i++)
			cout<<queue[i];
		cout<<endl;
	}
}
