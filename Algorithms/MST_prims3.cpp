#include <iostream>
#include <conio.h>
using namespace std;
struct node // solution mst: array of objects
{
    int fr, to, cost;
} p[6]; // sol vector
int c = 0, temp1 = 0, temp = 0;

int b[7][7];

void prims(int *parent)
{
    int i = 0, j = 0,tot_cost =0; // iterators
    parent[i] = 1;
    while (c < 6) // loop runs till soln vector is not containing all nodes of the graph
    {
        int min = 999;
        for (int i = 0; i < 7; i++)// go through all vertices of graph
        {
            if (parent[i] == 1)
            {
                for (int j = 0; j < 7;)
                {
                    if (b[i][j] >= min || b[i][j] == 0)
                    {
                        j++;
                    }
                    else if (b[i][j] < min)
                    {
                        min = b[i][j];
                        temp = i;
                        temp1 = j;
                    }
                }
            }
        }
        parent[temp1] = 1;
        p[c].fr = temp;
        p[c].to = temp1;
        p[c].cost = min;
        c++;
        b[temp][temp1] = b[temp1][temp] = 1000;		//make edge useless after reading
    }
    for (int k = 0; k < 6; k++)
    {
        cout << p[k].fr << "->" << p[k].to << endl;
        cout << "weight of node" << p[k].cost << endl;
        tot_cost = tot_cost + p[k].cost;
    }
    cout<<"Total cost :"<<tot_cost;
}
void read()
{
	int i,j,n;
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
				cin>>b[i][j];
		}
	}
}
int main()
{
    int parent[7];
    for (int i = 0; i < 7; i++)
    {
        parent[i] = 0;
    }
    
    read();
    prims(parent);
    getch();
}
//0 3 6 0 0 0 0 3 0 2 4 0 0 0 6 2 0 1 4 2 0 0 4 1 0 2 0 4 0 0 4 2 0 2 1 0 0 2 0 2 0 1 0 0 0 4 1 1 0
