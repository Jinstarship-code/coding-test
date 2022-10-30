#include <bits/stdc++.h>

using namespace std;

int n;


vector<int> v;

int main()
{
	cin >> n;
	int max_number = -1;

	for (int i = 0; i < n; ++i)
	{
		int x;
		cin >> x;
		v.push_back(x);
	}

	for (int i = 0; i < n-1; ++i)
	{
		int cnt = 0;
		for (int j = i+1; j < n; ++j)
		{
			if (v[i] > v[j])
			{
				cnt++;
			}
			else if (v[i] < v[j])
				break;
		}

		max_number = max(max_number, cnt);
	}

	cout << max_number;
	return 0;
}