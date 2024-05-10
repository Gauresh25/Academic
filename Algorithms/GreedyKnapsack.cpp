#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
int n,cap;
float x[10] = {0};

class item
{
	public:
	int objNo;
	float p;
	float w;
	float ratio;
};
item arr[10];

void display()
{
	cout<<"Object Value  Weight  Ratio  "<<endl;
	for(int i = 0;i<n;i++)
	{
	cout<<arr[i].objNo<<"\t"<<arr[i].p<<"\t"<<arr[i].w<<"\t"<<arr[i].ratio<<"\t"<<endl;
	}
	
}

void BubbleSort()
{
	item temp;
	int i,j;
    for (i = 0; i < n - 1; i++) 
	{
        for (j = 0; j < n - i - 1; j++) 
        {   if (arr[j].ratio < arr[j + 1].ratio) 
            {   temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
			}
		}
	}
}
void GreedyKnap()
{
	float remCap = cap;
	float profit = 0;
	int i = 0;
	for (i = 0; i < n; i++) 
	{
		if(arr[i].w>remCap)
			break;
			
		x[i]=1;
		remCap = remCap-arr[i].w;
	}
	if(i<=n)
	{
		x[i] = remCap / arr[i].w;
	}
	
	cout<<"Sloution vector: \n Items:  \t";
	for (i = 0; i < n; i++) 
	{
		cout<<arr[i].objNo<<"\t";
		profit += x[i]*arr[i].p;
	}
	cout<<"\nPortions\t";
	for (i = 0; i < n; i++) 
		cout<<x[i]<<"\t";
	cout<<"\n\nTotal profit "<<profit;
}

int main()
{
	cout<<"Enter knapsack capacity ";
	cin>>cap;
	cout<<"Enter no. of items ";
	cin>>n;
	
	for(int i = 0;i<n;i++)
	{
		arr[i].objNo = i+1;
		cout<<"\n\nEnter value of object "<<i+1<<" : ";
		cin>>arr[i].p;
		cout<<"Enter weight of object "<<i+1<<" : ";
		cin>>arr[i].w;
		
		arr[i].ratio = arr[i].p/arr[i].w;
	}
	display();
	
	cout<<"Sorted items: \n";
	BubbleSort();
	display();
	
	GreedyKnap();
}
