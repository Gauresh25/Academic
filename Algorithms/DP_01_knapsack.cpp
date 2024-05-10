#include <iostream>
#include <cstring>
using namespace std;

int v[6]={0,18,25,27,10,15};
int w[6]={0,3,5,4,3,6};
int value[20][20];
char keep[20][20];
int W=12,n=5;

void knapsack()
{
	int i,j;
	//
	
	for(int i=0 ; i<=W ; i++)
	{
		value[0][i]=0;
	}
	for(int j=0 ; j<=n ; j++)
	{
		value[j][0]=0;
	}
	for(i = 1;i<=n;i++)
	{
		for(j = 1;j<=W;j++)
		{
			if(w[i]<=j)//wt less then cap
			{
				if(v[i]+value[i-1][j-w[i]]>value[i-1][j])
				//if adding value is better than prev soln excluding it
				{
					value[i][j] = v[i] + value[i-1][j-w[i]];
					keep[i][j] = 'Y';
				}
				else
				{
					value[i][j] = value[i-1][j];
					keep[i][j] = 'N';
				}
			}
			else//contraint violated no point in proceeding
			{
				value[i][j] = value[i-1][j];
				keep[i][j] = 'N';
			}
		}
	}
}

void disp()
{
	int i,j;
	for (i=0;i<=n;i++)
	{
		for (j=0;j<=W;j++)
		{
			cout << value[i][j] <<keep[i][j] <<"\t";
		}
		cout <<"\n";
	}
}

void printKnap()
{
	int wt = W;
	
	for(int i = n;i>=0;i--)
	{
		if(wt>0&&keep[i][wt] == 'Y')
		{
			cout<<i<<endl;
			wt = wt -w[i];
		}
	}
}

int main()
{
	knapsack();
	//cout << "Length of subsequence :"<<subseq<<endl;
	disp();
	printKnap();

	return 0;
}

