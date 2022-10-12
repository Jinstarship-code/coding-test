#include <iostream>
#include <vector>

using namespace std;

struct body {
	int length;
	int cnt;
};

int main()
{
	body b1;
	body b2;
	body b3;
	int l;
	vector<body> a;
	int count=0;
	int sum_length = 0;
	cin >> b1.length >> b2.length >> b3.length;
	cin >> b1.cnt >> b2.cnt >> b3.cnt;
	cin >> l;

	if (b1.length > b2.length)
	{
		if (b1.length > b3.length)
		{
			a.push_back(b1);
			
			if (b2.length > b3.length)
			{
				a.push_back(b2);
				a.push_back(b3);
			}
			else
			{
				a.push_back(b3);
				a.push_back(b2);
			}
		}
		else
		{
			a.push_back(b3);
			a.push_back(b1);
			a.push_back(b2);
		}
	}
	else
	{
		if (b2.length < b3.length)
		{
			a.push_back(b3);
			a.push_back(b2);
			a.push_back(b1);
		}
		else
		{
			a.push_back(b2);
			if (b1.length > b3.length)
			{
				a.push_back(b1);
				a.push_back(b3);
			}
			else
			{
				a.push_back(b3);
				a.push_back(b1);
			}
		}
	}

	for (int i = 0; i < a.size(); ++i)
	{
		if (a[i].length > l)
			continue;

		// 다해도 못넘을때
		if (sum_length+a[i].length * a[i].cnt < l)
		{
			count += a[i].cnt;
			sum_length += a[i].length * a[i].cnt;
		}
		else if (sum_length + a[i].length * a[i].cnt > l)
		{
			int tmp_length = l-sum_length;
			int tmp_count = tmp_length / a[i].length;
			
			sum_length += a[i].length * tmp_count;
			if (sum_length == l)
			{
				count += tmp_count;
			}
			else
			{
				count += tmp_count + 1;
				sum_length += a[i].length;
			}
			break;
		}
		else
		{
			count += a[i].cnt;
			sum_length += a[i].length * a[i].cnt;
			break;
		}
	}
	
	if (sum_length < l)
		cout << 0;
	else
		cout << count;


	return 0;
}