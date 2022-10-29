#include <bits/stdc++.h>

using namespace std;

int n;
vector<int> v;

int main()
{
	cin >> n;

	for (int i = 0; i < n; ++i)
	{
		int x;
		cin >> x;
		v.push_back(x);
	}

	reverse(v.begin(), v.end());

	int dp[2000];
	for (int i = 0; i < n; ++i)
	{
		dp[i] = 1;
	}

	for (int i = 1; i < n; ++i)
	{
		for (int j = 0; j < i; ++j)
		{
			if (v[j] < v[i])
				dp[i] = max(dp[i], dp[j] + 1);
		}
	}

	int max_value = 0;

	for (int i = 0; i < n; ++i)
		max_value = max(max_value, dp[i]);

	cout << n - max_value;


	return 0;
}