#include <iostream>
#include <cstring>
#include <algorithm>
#include <math.h>
#include <bits/stdc++.h>
using namespace std;
int d =10;

void search(char pat[], char txt[], int q)
{
	int M = strlen(pat);
	int N = strlen(txt);
	int i, j;
	int p = 0; // hash value for pattern
	int t = 0; // hash value for txt
	int h = 1;

	h = int(pow(d, M-1))%q;

	for (i = 0; i < M; i++) {
		p = (d * p + pat[i]) % q;
		t = (d * t + txt[i]) % q;
	}
	cout<<"Pattern hash code: "<<p<<endl;

	for (i = 0; i <= N - M; i++) {

		cout<<"Rolling hash code at shift "<<i<<": "<<t<<endl;
		if (p == t) {
			for (j = 0; j < M; j++) {
				if (txt[i + j] != pat[j]) {
					break;
				}
			}


			if (j == M)
				cout << "Pattern found at shift " << i <<endl;
		}

		if (i < N - M) {
			t = (d * (t - txt[i] * h) + txt[i + M]) % q;

			if (t < 0)
				t = (t + q);
		}
	}
}

int main()
{
	char txt[20];
	char pat[20];
	cout<<"Enter text: ";
	cin>>txt;
	cout<<"Enter pattern to search: ";
	cin>>pat;

	int q = 13;

	search(pat, txt, q);
	return 0;
}

