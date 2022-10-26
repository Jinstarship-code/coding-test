#include <bits/stdc++.h>

using namespace std;

int t;

int n, m;
int arr[20][20];
int dp[20][20];

int main()
{
	cin >> t;


	while (t--)
	{
		cin >> n >> m;

		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < m; ++j)
			{
				cin >> arr[i][j];
				dp[i][j] = arr[i][j];
			}
		}

		for (int j = 1; j < m; ++j)
		{
			for (int i = 0; i < n; ++i)
			{
				int up, line, down;
				if (i == 0)
					down = 0;
				else
					down = dp[i - 1][j - 1];

				if (i == n - 1)
					up = 0;
				else
					up = dp[i + 1][j - 1];

				line = dp[i][j - 1];
				dp[i][j] = dp[i][j] + max(down, max(line, up));
					
			}
		}

		int result = 0;
		for (int i = 0; i < n; ++i)
			result = max(result, dp[i][m - 1]);
		cout << result;



	}


	return 0;
}