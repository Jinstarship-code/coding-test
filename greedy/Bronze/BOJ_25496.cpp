#include <bits/stdc++.h>

using namespace std;

int p, n;
int cnt;
vector<int> v;
int main()
{
	cin >> p >> n;

	for (int i = 0; i < n; ++i)
	{
		int x;
		cin >> x;
		v.push_back(x);
	}
	
	if (p >= 200)
	{
		cout << 0;
		return 0;
	}

	sort(v.begin(), v.end());
	for (int i = 0; i < v.size(); ++i)
	{
		p += v[i];
		cnt++;
		if (p >= 200)
			break;
	}

	cout << cnt;
	return 0;
}