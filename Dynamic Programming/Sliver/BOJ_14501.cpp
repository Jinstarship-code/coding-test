#include <bits/stdc++.h>

using namespace std;

int n;
vector<int> t;
vector<int> p;

int dp[16];
int max_value;

int main()
{
	cin >> n;

	for (int i = 0; i < n; ++i)
	{
		int x, y;
		cin >> x >> y;
		t.push_back(x);
		p.push_back(y);
	}

	for (int i = n - 1; i >= 0; --i)
	{
		int time = t[i] + i;
		if (time <= n)
		{
			dp[i] = max(p[i] + dp[time], max_value);
			max_value = dp[i];
		}
		else
			dp[i] = max_value;
	}
	cout << max_value;

	return 0;
}