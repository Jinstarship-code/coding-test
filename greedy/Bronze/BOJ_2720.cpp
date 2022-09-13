#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;

	int a[4]{ 25,10,5,1 };
	while (T--)
	{
		int b[4]{};
		int tmp;
		cin >> tmp;
		

		for (int i = 0; i < 4; ++i)
		{
			b[i] = tmp / a[i];
			tmp %= a[i];
			cout << b[i] << ' ';
		}
		cout << '\n';
	}
	return 0;
}