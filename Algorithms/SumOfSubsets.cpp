#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;


int set[6]={5,10,12,13,15,18};
int m=30;
int x[6]; 
int n=6;

void display(int k)
{
	int i=0;
	cout<<"\n Set:\n";
	for(i =0;i<=k;i++)
	{
		cout<<x[i]<<"\t";
		//x[i]=0;
	}
	for(i=k ;i<n-1;i++)
	{
		cout<<"0\t";
	}
	cout<<"\n Set:\n";
}

int sum()
{
	int s = 0;
	for(int i =0;i<n;i++)
	{
		s += set[i];
	}
	return s;
}

void SOS(int sum,int k,int rem)
{
	x[k]=1;
	if(sum + set[k] == m)
	{	display(k);
		//cout<<"here";
	}
	else if(sum +set[k]+set[k+1]<=m)
	{
		SOS( sum+set[k] , k+1 ,rem-set[k]);
	}
	if((sum + rem -set[k]>=m)&&(sum +set[k]<=m))
	{
		x[k] = 0;
		SOS(sum,k+1,rem-set[k]);
	}
}

int main()
{
	SOS(0,0,sum());
}
