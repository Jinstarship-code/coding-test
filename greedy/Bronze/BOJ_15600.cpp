#include <iostream>

using namespace std;

int main()
{
	int n;
	cin >> n;

	if (n <= 3)
		cout << 1;
	else
		cout << n - 2;
	return 0;
}