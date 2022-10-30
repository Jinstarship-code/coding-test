#include <bits/stdc++.h>

using namespace std;

int n,cnt;
queue<int> q;

int main()
{
	cin >> n;
	for (int i = 0; i < n; ++i)
	{
		int x;
		cin >> x;
		q.push(x);
	}
	int stay_number = 1;

	while (!q.empty())
	{
		if (stay_number == q.front())
		{
			stay_number++;
			q.pop();
			
			continue;
		}
		
		q.pop();
		cnt++;
	}
	

	cout << cnt;
	return 0;
}