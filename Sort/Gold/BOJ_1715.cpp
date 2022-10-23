#include <bits/stdc++.h>

using namespace std;

int n;
priority_queue<int> pq;
int result;
int main()
{
	cin >> n;
	while (n--)
	{
		int x;
		cin >> x;
		pq.push(-x);
	}
	
	while (pq.size() != 1)
	{
		int one = -pq.top();
		pq.pop();
		int two = -pq.top();
		pq.pop();

		int sum = one + two;
		result += sum;
		pq.push(-sum);
	}
	cout << result;



	return 0;
}