#include <iostream>
#include <cstring>
// 0 0 6 3 0 3 0 0 0 0 0 0 0 2 0 0 1 1 0 0 0 4 0 2 0 
using namespace std;

int G[10][10];
int D[10],P[10];
int edge[10][3];
int n,eCount=0;
int source,inf = 999;;

int parent[10];//predescessor matrix
/*class node // solution mst: array of objects
{
    int fr, to, cost;
} mst[10]; // sol vector*/
int MST[10];//boolean  arr if node in mst
int key[10];//min weight of vertex i 

void prims()
{
	for(i = 0;i<n;i++)	//init all key to infinity and no node in mst
	{
		key[i]=inf;
		MST[v]=0;
	}
	key[0] = 0;
	parent[0] = -1;//first node added to mst
	for(i = 0;i<n;i++)
	{
		k = //std::min_element(key, key + n)
		}
	}
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
