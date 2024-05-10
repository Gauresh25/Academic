#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int x[20];
int n;
int soln=0;
int calls = 0;

bool place(int k,int i)
{
	for(int j=1;j<=k-1;j++)
	{
		if((x[j]==i)||(abs(x[j]-i)==abs(j-k)))
		{return false;}
	}
	return true;
}

void display()
{
	cout<<"\n Positions:\n";
	for(int i =1;i<=n;i++)
	{
		cout<<x[i]<<"\t";
	}
	cout<<"\n Matrix: \n";
	for(int i = 1;i<=n;i++)
	{
		for(int j = 1;j<=n;j++)
		{
			if(j==x[i])
				cout<<" Q ";
			else 
				cout<<" _ ";
		}
		cout<<"\n";
	}
}

void NQueens(int k,int n)
{
	calls++;
	for(int i=1;i<=n;i++)
	{
		//cout<<k<<endl;
		if(place(k,i)==true)
		{
			x[k]=i;
			if (k==n)
			{	display();
				soln++;
			}
			else
			{	NQueens(k+1,n);}
			//cout<<"here";
		}
		
	}
}


int main()
{
	for(int iter = 0;iter<20;iter++)
	{
	x[iter] = 0;
	}
	cout<<"Enter n: ";
	cin>>n;
	NQueens(1,n);
	cout<<"Possible Solutions: "<<soln<<"\n";
	cout<<"Nodes in tree: "<<calls;
	return 0;
}
