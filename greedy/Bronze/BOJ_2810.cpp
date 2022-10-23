#include <iostream>
#include <vector>
#include <string>

using namespace std;

int n;
string str;
vector<char> a;

int main()
{
	cin >> n;
	
	a.push_back('*');
	cin >> str;

	for (int i = 0; i < str.length(); ++i)
	{
		if (str[i] == 'S')
		{
			a.push_back(str[i]);
			a.push_back('*');
		}
		else if (str[i] == 'L')
		{
			a.push_back(str[i]);
			a.push_back(str[i]);
			a.push_back('*');
			i++;
		}
	}

	if(a[a.size()-1] != '*')
		a.push_back('*');

	int count = 0;

	for (int i = 0; i < a.size(); ++i)
		if (a[i] == '*')
			count++;

	if (n > count)
		cout << count;
	else
	{
		cout << n;
	}

	return 0;
}