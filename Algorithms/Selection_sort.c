#include <stdio.h>
//#include <conio.h>

int arr[10],n;


void read(int n)
{
	int i;
	for(i = 0;i<n;i++)
	{
		scanf("%d",&arr[i]);
	}
}

void display()
{
	int i;

	for(i = 0;i<n;i++)
	{
		printf("%d ",arr[i]);
	}
}

void sel_sort()
{
	int i,j,k,temp,comp=0,swaps = 0;
	for(i=0;i<n;i++)	//i points to last location of sorted array
	{
		j=i;
		for(k = i+1;k<n;k++)	//k travels unsorted portion to find smallest element
		{
			comp++;
			if (arr[k] < arr[j])
			{
				j=k;			//j now points to smallest element
				
			}
		}
		if(j != i)
		{	temp = arr[j];
			arr[j] = arr[i];	//swap
			arr[i] = temp;
			swaps++;
		}
		printf("\nIteration %d :",i+1);
		display();
	}
	printf("\nTotal comparison %d ",comp);
	printf("\nTotal swaps %d ",swaps);
}

int main()
{
	printf("Enter number of elements :");
	scanf("%d",&n);
	read(n);
	printf("Array is :\n");
	display();
	sel_sort();
	
	return 0;
}
