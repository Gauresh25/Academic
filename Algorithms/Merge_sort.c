#include <stdio.h>
#include <math.h>

int arr[6]={1,3,5,2,4,6};
int n =6;


void read(int n)
{
	int i;
	for(i = 0;i<n;i++)
	{
		scanf("%d",&arr[i]);
	}
}

void display(int l,int h)
{
	int i;
	printf("\n ");
	for(i = l;i<h;i++)
	{
		printf("%d ",arr[i]);
	}
}

void merge(int low,int mid,int high)
{
	int h,i,j,k;
	int temp[n]={};
	h = low;	//travel left array
	i = low;	//travel result array
	j = mid+1;	//travel right array
	while(h<=mid && j<high)
	{
		printf("\n %d %d \n",h,j);
		if(arr[h]<=arr[j])
		{	temp[i++] = arr[h++];}
		else
		{	temp[i++] = arr[j++];}
		
	}
	/*
	if (h>mid)								//array exhausted
	{
		for(k=j;k<=high;k++)////
		{	temp[i++] = arr[k];}
	}
	else{
		for(k=h;k<=mid;k++)
		{	temp[i++] = arr[k];}
	}*/
	
	for(k=low;k<high;k++)					//putting in og array
		{	arr[k] = temp[k];
			printf(" %d ",temp[k]);
		}
		
	display(low,high);
}

void merge_sort(int low,int high)
{
	if (low<high)
	{	int mid; 
		mid=ceil((low +high)/2);
		merge_sort(low,mid);
		merge_sort(mid+1,high);
		merge(low,mid,high);
		//printf("here"); 
	}
}

int main()
{
	/*printf("Enter number of elements :");
	scanf("%d",&n);
	*/
	
	
	printf("Array is :\n");
	display(0,n);
	merge(0,n/2,n);
	//merge_sort(0,n)	;
	display(0,n);
	//printf("\n11 22 33 44");
	return 0;
}
