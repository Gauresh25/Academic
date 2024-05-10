#include <iostream>
#include <cstring>
using namespace std;

char str1[20]="ABCBDAB",str2[20]="BDCABA";
int count[20][20];
char backptr[20][20];
int m,n;

void LCS_len()
{
	int m,n,i,j;
	m=strlen(str1);
	n=strlen(str2);
	//
	
	for(int i=0 ; i<=m ; i++)
	{
		count[i][0]=0;
	}
	for(int j=0 ; j<=m ; j++)
	{
		count[0][j]=0;
	}
	for(i = 1;i<=m;i++)
	{
		for(j = 1;j<=n;j++)
		{
			if(str1[i-1] == str2[j-1])		//loop runs from 1,strin indexing strarts from 0
			{
				count[i][j]=count[i-1][j-1]+1;
				backptr[i][j] = 'D';
			}
			else if(count[i-1][j] >=count[i][j-1])
			{
				count[i][j] = count[i-1][j];
				backptr[i][j] = '^';
			}
			else
			{
				count[i][j] = count[i][j-1];
				backptr[i][j] = '<';
			}
		}
	}
}

void disp()
{
	int i,j;
	for (i=0;i<=m;i++)
	{
		for (j=0;j<=n;j++)
		{
			cout << count[i][j] <<backptr[i][j] <<"\t";
		}
		cout <<"\n";
	}
}

void printLCS(int i,int j)
{
		if(i==0||j==0)
		{
			return;
			
		}
		if(backptr[i][j] == 'D')
		{
			printLCS(i-1,j-1);
			cout<<str1[i-1];
		}	
		else if(backptr[i][j] == '^')
		{
			printLCS(i-1,j);
		}
		else
		{
			printLCS(i,j-1);
		}
		
}

int main()
{
	int subseq;
	cout << "Enter the 2 strings\n";
	
	m=strlen(str1);
	n=strlen(str2);
	
	LCS_len();
	
	subseq = count[m][n];
	cout << "Length of subsequence :"<<subseq<<endl;
	disp();
	printLCS(m,n);

	return 0;
}
