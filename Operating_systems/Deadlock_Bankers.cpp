#include <iostream>
#include <conio.h>

using namespace std;

class proc
{
	public:
	int max[3];
	int alloc[3];
	int need[3];
	int fl = 0;
}li[5];

int ans[5];
int ind = 0;
int n =5;
int avail[3] ={3,3,2};
int m = 3;

bool isSafe()
{
	for(int  i = 0;i<n;i++)
	{
		if(li[i].fl == 0)
		{
			cout<<"unsafe state";
			return false;
		}
	}
	return true;
}
int main()
{
	/*li[0].alloc={0,1,0};
	li[1].alloc={2,0,0};
	li[2].alloc={3,0,2};
	li[3].alloc={2,1,1};
	li[4].alloc={0,1,0};
	
	li[0].max={7,5,3};
	li[1].max={3,2,2};
	li[2].max={9,0,2};
	li[3].max={2,2,2};
	li[4].max={4,3,3};*/
	
	cout<<"enter alloc"<<endl;
	for(int i = 0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
				cin>>li[i].alloc[j];
		}
	}
	cout<<"enter max"<<endl;
	for(int i = 0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
				cin>>li[i].max[j];
		}
	}
	
	for(int i =0;i<n;i++)
	{
		for(int j=0;j<m;j++)
			li[i].need[j] = li[i].max[j] -li[i].alloc[j];
	}
	
	for(int k = 0;k<n;k++)
	{	
	for(int i =0;i<n;i++)
	{
		if(li[i].fl==0)
		{
			//check if aloocateable
			int flag =0;
			for(int j=0;j<m;j++)
			{
				if(li[i].need[j]>avail[j])
					flag = 1;//not allocable
			}
			
			if(flag == 0)
			{
				ans[ind++]= i;
				//update alloc
				for(int j=0;j<m;j++)
					avail[j] = avail[j] + li[i].alloc[j];
				li[i].fl=1;
			}
		}
	}
	}
	
	if(isSafe())
	{
		for(int i = 0;i<ind;i++)
		cout<<ans[i]<<"  ";}
	
	return 0;
}
