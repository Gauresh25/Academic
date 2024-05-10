#include <iostream>
#include <conio.h>
#include <queue>
using namespace std;

class pcb
{
	public:
	int arr=0;
	int burst;
	int bt;
	int comp;
	int wait;
	int turnaround;
}proc[10],temp;
queue<pcb> RQ;

int main()
{
	int n,total;
	
	float total_tat = 0;
	float total_wt = 0;
	int q;
	cout<<"Enter no. of processes";
	cin>>n;
	cout<<"Enter time slot";
	cin>>q;	
		
	cout<<"Enter burst time of processes in order of arrival"<<endl;
	for(int i =0;i<n;i++)
	{
		cout<<"Enter burst time of process "<<i<<endl;
		cin>>proc[i].burst;
		proc[i].bt=proc[i].burst;
		total =total + proc[i].burst;
	}
	for(int i =0;i<n;i++)
	{
		RQ.push(proc[i]);
	}
	
	int time = 0;
	
	while(!RQ.empty())
	{
		temp = RQ.front();
		RQ.pop();
		int exec = min(q,temp.burst);
		time = time + exec;
		temp.burst = temp.burst - exec;
		if(temp.burst <=0)
		{
			temp.comp = time+temp.burst;
			temp.turnaround = temp.comp - temp.arr;
			temp.wait = temp.turnaround - temp.bt;
			total_tat= total_tat+ temp.turnaround;
			total_wt = total_wt + temp.wait;
		}
		else
		{
			RQ.push(temp);
			
		}
		cout<<temp.burst<<" "<<temp.turnaround<<" "<<temp.wait<<endl<<endl;
	}
	/*for(int i =0;i<n;i++)
	{
		cout<<proc[i].burst<<" "<<proc[i].turnaround<<" "<<proc[i].wait<<endl; 
		total_tat= total_tat+proc[i].turnaround;
		total_wt = total_wt + proc[i].wait;
	}*/
	cout<<"total turnaround "<<total_tat<<endl;
	cout<<"total waiting "<<total_wt<<endl;
	
	cout<<"Avg turnaround "<<total_tat/n<<endl;
	cout<<"avg waiting "<<total_wt/n;
	return 0;
}
