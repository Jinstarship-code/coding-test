#include <bits/stdc++.h>

using namespace std;

int l, p, v;
vector<int> vec;
int main()
{
	while (true)
	{
		int result;
		cin >> l >> p >> v;

		if (l == 0 && p == 0 && v == 0)
			break;

		int div = v / p;
		int mod = v % p;
		result = div * l;

		if (l >= mod)
			result += mod;
		else
			result += l;

		vec.push_back(result);
	}

	for (int i = 0; i < vec.size(); ++i)
		cout << "Case " << i+1 << ": " << vec[i]<<'\n';

	return 0;
}