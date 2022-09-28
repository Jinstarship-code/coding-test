#include <iostream>

using namespace std;

int main()
{
	int n;
	cin >> n;
	int max = -1;
	int sum = 0;
	while (n--)
	{
		int tmp;
		cin >> tmp;

		if (max < tmp)
			max = tmp;
		sum += tmp;
	}

	cout << sum - max;


	return 0;
}