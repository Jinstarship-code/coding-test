#include <bits/stdc++.h>

using namespace std;

int n;


int main()
{
	while (true)
	{
		int a[6]{};
		int b[6]{};
		int a_odd = 0, a_even = 0;
		int b_odd = 0, b_even = 0;

		cin >> n;
		if (n == 0)
			break;

		for (int i = 0; i < n; ++i)
		{
			int x;
			cin >> x;
			a[x]++;
			if (x % 2 == 0)
				a_even++;
			else
				a_odd++;
		}
		for (int i = 0; i < n; ++i)
		{
			int x;
			cin >> x;
			b[x]++;
			if (x % 2 == 0)
				b_even++;
			else
				b_odd++;
		}
		
		cout << abs(a_even - b_odd)<<'\n';


	}

	return 0;
}


/*

  a_odd = 8 a_even = 1
  b_odd = 5 b_even = 4

*/