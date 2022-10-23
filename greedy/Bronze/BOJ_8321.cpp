#include <bits/stdc++.h>

using namespace std;

int n, k, s;
int result;
vector<int> v;

int main()
{
	cin >> n >> k >> s;
	for (int i = 0; i < n; ++i)
	{
		int x;
		cin >> x;
		v.push_back(x);
	}

	sort(v.begin(), v.end(), greater<>());

	s *= k;
	
	while (s > 0)
	{
		for (int i = 0; i < v.size(); ++i)
		{
			s -= v[i];
			result++;
			if (s <= 0)
				break;
		}
	}
	cout << result;

	return 0;
}