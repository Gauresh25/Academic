#include <stdio.h>

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
	printf("\n ");
	for(i = 0;i<n;i++)
	{
		printf("%d ",arr[i]);
	}
}

void ins_sort()
{
	int i,temp,j,swaps = 0;
	for(j = 1; j<n;j++)
	{
		i = j-1;			//i traverses sorted array in reverse manner
		temp = arr[j];
		while (i>=0 && arr[i]>temp)
		{
			arr[i+1] = arr[i];
			i=i-1;
			swaps++;
		}
		arr[i+1] = temp;
		display();
	}
	printf("\nTotal swaps %d ",swaps);
}

int main()
{
	printf("Enter number of elements :");
	scanf("%d",&n);
	read(n);
	printf("Array is :\n");
	display();	
	ins_sort();
	display();

	return 0;
}
