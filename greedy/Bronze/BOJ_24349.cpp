#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int n, a, b, c;
	cin >> n >> a >> b >> c;

	long long result = 0;
	if (n == 1)
	{
		cout << 0 << " " << 0;
	}
	else
	{
		int tmp= min(a, b);
		int min_length = min(tmp, c);
		n--;
		if (min_length == c)
		{
			result += tmp;
			n--;
			result += min_length * n;
		}
		else
		{
			result += min_length * n;
		}
	}

	cout << result / 100 << ' ' << result % 100;
	return 0;
}

/*

	토끼 - 올뺴미 : a
	토-요 : b
	올-요 : c

	토끼 스타트

	8
	7 56
	6 56 56
	5 56 56 56
	4 56 56 56 56
	3 56 56 56 56 56
	2 56 56 56 56 56 56
	1 56 56 56 56 56 56 56
	0 56 56 56 56 56 56 56 56
	
*/

