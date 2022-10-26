#include <bits/stdc++.h>

using namespace std;


int n;

int arr[500][500];
int dp[500][500];

int main()
{
	cin >> n;
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < i+1; ++j)
		{
			cin >> arr[i][j];
			dp[i][j] = arr[i][j];
		}
	}

	
	for (int i = 1; i < n; ++i)
	{
		for (int j = 0; j < i + 1; ++j)
		{
			if (j == 0)
				dp[i][j] = arr[i][j] + dp[i - 1][j];
			else if (j == i)
				dp[i][j] = arr[i][j] + dp[i - 1][j-1];
			else
			{
				dp[i][j] = arr[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j]);
			}


		}
	}
	int result=-1;
	for (int j = 0; j < n; ++j)
		result = max(result, dp[n - 1][j]);
	cout << result;
	return 0;
}