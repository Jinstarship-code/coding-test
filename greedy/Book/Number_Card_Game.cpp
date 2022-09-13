#include <iostream>

using namespace std;

int main()
{
	int n, m;
	cin >> n >> m;
	int a[101][101]{};
	int b[101]{};
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < m; ++j)
		{
			cin >> a[i][j];
		}

		for (int j = 0; j < m-1; ++j)
		{
			if (a[i][j] <= a[i][j + 1])
			{
				b[i] = a[i][j];
			}
		}
	}
	int max = INT_MIN;
	for (int i = 0; i < n; ++i)
	{
		if (max < b[i])
		{
			max = b[i];
		}
	}
	cout << max;
	return 0;
}