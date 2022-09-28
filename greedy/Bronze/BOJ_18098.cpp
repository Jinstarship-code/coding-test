#include <iostream>

using namespace std;

int main()
{
	int n;
	cin >> n;
	bool a[100001]{};
	int cnt = 0;
	int b = n;
	while (n--)
	{
		int tmp;
		cin >> tmp;
		
		if(tmp < 100001)
			a[tmp] = true;
	}

	for (int i = 1; i <= b; ++i)
	{
		if (a[i] == true)
			cnt++;
	}
	cout << cnt;
	return 0;
}