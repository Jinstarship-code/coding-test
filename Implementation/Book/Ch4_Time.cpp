#include <iostream>
#include <string>
using namespace std;

int main()
{
	int n;
	cin >> n;

	int cnt = 0;
	for (int i = 0; i <= n; ++i)
	{
		for (int j = 0; j < 60; ++j)
		{
			for (int k = 0; k < 60; ++k)
			{
				if (i % 10 == 3 || j % 10 == 3 || j / 10 == 3 || k % 10 == 3 || k / 10 == 3)
					cnt++;
			}
		}
	}
	cout << cnt;


	return 0;
}