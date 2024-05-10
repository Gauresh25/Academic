#include <iostream>
#include <conio.h>
using namespace std;

class pcb
{
	public:
	int arr=0;
	int burst;
	int comp;
	int wait;
	int turnaround;
}proc[10];

int main()
{
	int n,total;
	
	float total_tat = 0;
	float total_wt = 0;
	cout<<"Enter no. of processes";
	cin>>n;
	
	cout<<"Enter burst time of processes in order of arrival";
	for(int i =0;i<n;i++)
	{
		cout<<"Enter burst time of process "<<i;
		cin>>proc[i].burst;
		total =total + proc[i].burst;
	}
	int time = 0;

	for(int i =0;i<n;i++)
	{
		time = time + proc[i].burst;
		proc[i].comp = time;
		proc[i].turnaround=proc[i].comp-proc[i].arr;
		proc[i].wait = proc[i].turnaround - proc[i].burst;
		total_tat = total_tat+proc[i].turnaround;
		total_wt = total_wt + proc[i].wait;
	}
	cout<<total_tat/n;
	cout<<total_wt/n;
	return 0;
}

