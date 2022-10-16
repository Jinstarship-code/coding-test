#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int n;
char arr[1000000];

int main()
{
	cin >> n;

	string str_n=to_string(n);
	

	for (int i = 0; i < str_n.length(); ++i)
	{
		arr[i] = str_n[i];
	}

	sort(arr, arr + str_n.length(),greater<char>());

	for (int i = 0; i < str_n.length(); ++i)
		cout << arr[i];
	return 0;
}