#include <iostream>
#include <cstring>
// 0 0 6 3 0 3 0 0 0 0 0 0 0 2 0 0 1 1 0 0 0 4 0 2 0 
using namespace std;

int G[10][10];
int D[10],P[10];
int edge[10][3];
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

void edgeT()
{
	int i,j;
	for(i = 0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			if(i!=j && G[i][j]!=0)
			{
				edge[eCount][0] = i;
				edge[eCount][1] = j;
				edge[eCount][2] = G[i][j];
				eCount++;
			}
		}
	}
}

void printEdge()
{
	int i;
	for(i = 0;i<eCount;i++)
	{
		cout<<edge[i][0]<<" -> "<<edge[i][1]<<" : "<<edge[i][2];
		cout<<"\n";
	}
}

void Initialize(int s)
{
	for(int i =0;i<n;i++)
	{
		D[i]=inf;
		P[i]=-1;
	}
	D[s]=0;
}

void relax(int src,int des,int weight)
{
	if(D[src] + weight< D[des])
	{	
		D[des] = D[src] + weight;
		P[des] = src;
	}
}

void print_D_Pi(int source)
{
	cout<<"D and pi array:\n"; 
	for(int i = 0;i<n;i++)
	{
		if(i != source)
			cout<<"vertex: "<<i<<" D:"<<D[i]<<" pred:"<<P[i]<<"\n";
	}
}

void BellmanFord(int source)
{
	Initialize(source);
	print_D_Pi(source);
	
	for(int i =0;i<n;i++)
	{
		for(int j = 0;j<eCount;j++)
		{
			relax(edge[j][0],edge[j][1],edge[j][2]);
		}
	}
	print_D_Pi(source);
	//negative cycle check
	for(int j = 0;j<eCount;j++)
	{
		if(D[edge[j][1]] > D[edge[j][0]]+edge[j][2])
		{
			cout<<"Negative cycle exists";
			exit(0);
		}
	}
}

void printPath(int vert)
{
	if(vert == source)
		cout<<"\n"<<source;
	else if(P[vert] == -1)
		cout<<"\nunreachable";
	else
	{
		printPath(P[vert]);
		cout<<" -> "<<vert;
	}
}

int main()
{
	read();
	display();
	edgeT();
	printEdge();
	
	cout<<"Enter source vertex: ";
	cin>>source;
	
	BellmanFord(source);
	for (int i = 0;i<n;i++)
	{	
		if (i!=source)
			printPath(i);
	}
	return 0;
}
