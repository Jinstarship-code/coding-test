#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	vector<int> a, b;
	vector<int> c;

	int n, m;
	cin >> n >> m;
	int win = 0;
	int cnt = 0, money = 0;

	for (int i = 0; i < m; ++i)
	{
		int tmpA, tmpB;
		cin >> tmpA >> tmpB;
		a.push_back(tmpA);
		b.push_back(tmpB);
		if (tmpA < tmpB)
			c.push_back(tmpB - tmpA);
	}

	for (int i = 0; i < m; ++i)
	{
		if (a[i] >= n)
			win++;
	}

	if (win >= m - 1)
	{
		cout << 0;
		return 0;
	}
	cnt = m - 1 - win;

	sort(c.begin(), c.end());

	for (int i = 0; i < cnt; ++i)
	{
		money += c[i] / 2;
	}
	cout << money;
	return 0;
}

/*
	8칸인 5장의 포인트카드

	1 7   6  3
	6 2  -4
	3 5   2  1
	4 4   0
	0 8   8

*/