#include <bits/stdc++.h>

using namespace std;

int sign[50][5];
int n;

int main()
{
	cin >> n;
	
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < 5; ++j)
			cin >> sign[i][j];
	}
	
	int day = 0;
	int signed_officials = 0;
	
	for (int i = 0; i < n; ++i)
	{
		for (int j = day%7; j < 5; ++j)
		{
			day++;
			if (sign[i][j] == 1)
			{
				signed_officials++;
				break;
			}
		}

		if (n == signed_officials)
		{
			break;
		}
		else if (i == n - 1)
		{
			i = signed_officials-1;
			day += 2;
		}

	}
	
	cout << day;

	
	return 0;
}