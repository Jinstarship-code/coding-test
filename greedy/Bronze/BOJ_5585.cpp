#include <iostream>

using namespace std;

int main()
{
	int cnt = 0;
	int money;
	cin >> money;
	money = 1000 - money;
	int a[6]{ 500,100,50,10,5,1 };
	
	for (int i = 0; i < 6; ++i)
	{
		cnt += money / a[i];
		money %= a[i];
	}
	cout << cnt;
	return 0;
}