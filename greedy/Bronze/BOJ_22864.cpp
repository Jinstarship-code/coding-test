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

		// �޽ı�
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
	1hr work => +A�Ƿ�, +Bó��
	1hr rest => -C�Ƿ� > 0

	if �Ƿε� > M ==> burn out!!

	cf) 1day = 24hr, start 0


*/