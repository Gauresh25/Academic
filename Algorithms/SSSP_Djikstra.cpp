#include <iostream>
#include <cstring>
#include <bits/stdc++.h>
// 0 0 6 3 0 3 0 0 0 0 0 0 0 2 0 0 1 1 0 0 0 4 0 2 0 
using namespace std;

int G[10][10];

//int edge[10][3];
int n=5,eCount=0;
int source,inf = 999;
int q[10];

class calc
{
	public:
	int D;
	int P;
	bool vis = false;
}item[5];
class edges
{
	public:
	int src;
	int des;
	int wgt;
}edge[10];//edge table is a min proirity q

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
			/*if(i==j)
			{	
				cout<<"D";
				G[i][j] = 0;
				continue;
			}
			else*/
				cin>>G[i][j];
		}
	}
	j = 0;
}

void display()
{
	int i,j;
	for(i = 0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			if(i == j)
			{	G[i][j] = 0;}
			cout<<G[i][j]<<"\t";
		}
		cout<<"\n";
	}
}

void Initialize(int s)
{
	for(int i =0;i<n;i++)
	{
		item[i].D=inf;
		item[i].P=-1;
	}
	item[s].D=0;
}

void print_D_Pi(int source)
{
	cout<<"D and pi array:\n"; 
	for(int i = 0;i<n;i++)
	{
		if(i != source)
			cout<<"vertex: "<<i<<" D:"<<item[i].D<<" pred:"<<item[i].P<<"\n";
	}
}

void edgeT()
{
	int i,j;
	for(i = 0;i<10;i++)
	{
		for(j=0;j<n;j++)
		{
			if(i!=j && G[i][j]!=0)
			{
				edge[eCount].src = i;
				edge[eCount].des = j;
				edge[eCount].wgt = G[i][j];
				eCount++;
			}
		}
	}
}

void relax(int src,int des,int weight)
{
	if(item[src].D + weight< item[des].D)
	{	
		item[des].D = item[src].D + weight;
		item[des].P = src;
	}
}

void printPath(int vert)
{
	if(vert == source)
		cout<<"\n"<<source;
	else if(item[vert].P == -1)
		cout<<"\n vertex "<<vert<<" unreachable";
	else
	{
		printPath(item[vert].P);
		cout<<" -> "<<vert;
	}
}

int extMin()
{
	int ind = -1,min =999;
	int i;
	for(i =0;i<n;i++)
	{
		if(!item[i].vis && item[i].D<min)
		{
			min = item[i].D;
			ind = i;
		}
	}
	
	item[i].vis = true;
	return ind;
}

void Djikstra(int s)
{
	Initialize(s);
	edgeT();
	int u;
	for(int i = 0 ; i<n ; i++)
	{
		u = extMin();
		cout<<"process : "<<u<<endl;
		item[u].vis = true;
		for(int j = 0;j<eCount;j++)
		{
			if(edge[j].src == u)
			{
				relax(edge[j].src,edge[j].des,edge[j].wgt);
			}
		}
	print_D_Pi(s);
	}
}

int main()
{
	read();
	Djikstra(0);
	for (int i = 0;i<n;i++)
	{	
		if (i!=source)
			printPath(i);
	}
	return 0;
}
