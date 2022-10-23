#include <bits/stdc++.h>

using namespace std;

int n, w;
int result;
int tmp;
vector<int> v;

int main()
{
	cin >> n >> w;

	for (int i = 0; i < n; ++i)
	{
		int x;
		cin >> x;
		v.push_back(x);
	}


	for (int i = 0; i < v.size(); ++i)
	{
		tmp += v[i];
		if (tmp >= w)
		{
			result++;
			tmp = 0;
		}
	}

	cout << result;
	return 0;
}

//   2  1 