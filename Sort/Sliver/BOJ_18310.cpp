#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
vector<int> v;

int main()
{
	cin >> n;
	for(int i=0;i<n;++i)
	{
		int x;
		cin >> x;
		v.push_back(x);
	}

	sort(v.begin(), v.end());

	cout << v[(n- 1) / 2];
	return 0;
}