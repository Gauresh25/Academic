#include <stdio.h>

int arr[20];
int count=0;
int n=0;

void inputData()
{
	int i=0;
	printf("Enter Size of Array\n");
	scanf("%d",&n);
	printf("Enter array\n");
	for(i=0;i<n;i++)
	{
		scanf("%d",&arr[i]);
	}
	
}
void display()
{
	int i=0;
	printf("  \n  ");
	for(i=0;i<=n;i++)
	{
		printf("  %d  ",arr[i]);
	}
}

int partition(int p,int r)
{
	int x,i,j,temp;
	x = arr[r];
	i = p-1;
	for(j=p;j<r;j++)
	{
		if (arr[j]<=x)
		{
			i++;
			temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
		}
	}
	temp = arr[i+1];
	arr[i+1] = arr[r];
	arr[r] = temp;
	display();
	printf("\n%d",i+1);
	return (i+1) ;
}

void Quick(int p,int r)
{
	int q;
	if(p<r)
	{
		q=partition(p,r);
		Quick(p,q-1);
		Quick(q+1,r);
		
		count++;
	}
}
int main()
{
	inputData();
	
	printf("\nOrignal Data\n");
	display();
	Quick(0,n);
	display();
	

	printf("\nCount : %d\n",count);

	return 0;
}
