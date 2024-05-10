#include <iostream>
#include <cstring>
#include <algorithm>
// 0 5 0 2 0 0 0 2 0 0 3 0 0 0 7 0 0 4 0 1 1 3 0 0 0  
using namespace std;

int G[10][10];
int D[10][10],P[10][10];
//int edge[10][3];
int n,eCount=0;
int source,inf = 999;

void read()
{
	int i,j;
	cout<<"Enter no. of elements :";
	cin>>n;
	cout<<"Enter Adjacency matrix (0 for no edge)\n";
	for(i = 0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
				cin>>G[i][j];
				if (i==j)
				{
					G[i][j]=0;
				}
		}
	}
}

void Init()
{
	int i,j;
	for (i=0;i<n;i++)
	{	for (j=0;j<n;j++)
		{
			if(i!=j && G[i][j]==0)
			{
				D[i][j] = inf;
				P[i][j] = -1;
			}
			else
			{
				D[i][j] = G[i][j];
				P[i][j] = i;
				if(i==j)
					P[i][j] = -1;
			}
			
		}
	}
}


void display()
{
	int i,j;
	cout<<"Graph is \n";
	for(i = 0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			cout<<G[i][j]<<"\t";
		}
		cout<<"\n";
	}
	cout<<"D is \n";
	for(i = 0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			cout<<D[i][j]<<"\t";
		}
		cout<<"\n";
	}
	cout<<"P is \n";
	for(i = 0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			cout<<P[i][j]<<"\t";
		}
		cout<<"\n";
	}
}

void Floyd_Warshall()
{
	int i,j,k;
	Init();

	for(k = 0; k<n; k++)
	{
		for(i = 0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{
				//D[i][j] = min( D[i][j] , D[i][k]+D[k][j] );
				if (D[i][j] > D[i][k]+D[k][j])
				{	P[i][j] = P[k][j];}
				D[i][j] = min( D[i][j] , D[i][k]+D[k][j] );
			}
		}
		display();
	}
}

void printPath(int i,int j)
{
	if(i==j)
		cout<< i;
	else if(P[i][j] == inf)
		cout<<"unreachable";
	else
	{
		printPath(i,P[i][j]);
		cout<<" -> "<<j;
	}
}

int main()
{
	read();
	Floyd_Warshall();
	display();
	for (int i = 0;i<n;i++)
	{	
		for(int j=0;j<n;j++)
			{
				if (i!=j)
				{	printPath(i,j);
					cout<<"\n";
				}
			}
		cout<<"\n";
	}
}
