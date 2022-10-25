#include <bits/stdc++.h>

using namespace std;

int n, c;

vector<int> v;



int main()
{
	cin >> n >> c;

	for (int i = 0; i < n; ++i)
	{
		int x;
		cin >> x;
		v.push_back(x);
	}

	sort(v.begin(), v.end());

	int start = 1;
	int end = v[n - 1] - v[0];
	int result = 0;

	while (start <= end)
	{
		int mid = (start + end) / 2;

		int value = v[0];
		int cnt = 1;

		for (int i = 0; i < n; ++i)
		{
			if (v[i] >= value + mid)
			{
				value = v[i];
				cnt++;
			}
		}
		if (cnt >= c)
		{
			start = mid + 1;
			result = mid;
		}
		else
		{
			end = mid - 1;
		}
	}

	cout << result;
	return 0;
}