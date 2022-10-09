#include <iostream>

using namespace std;

int main()
{
	int a, b, c, m;
	cin >> a >> b >> c >> m;

	int workPerhr = 0;
	int tired = 0;
	for (int i = 0; i < 24; ++i)
	{
		if (a > m) break;

		// 휴식기
		if (tired + a > m)
		{
			tired -= c;
			if (tired < 0) tired = 0;
		}
		else
		{
			workPerhr += b;
			tired += a;
		}

	}
	cout << workPerhr;
	return 0;
}

/*
	1hr work => +A피로, +B처리
	1hr rest => -C피로 > 0

	if 피로도 > M ==> burn out!!

	cf) 1day = 24hr, start 0


*/