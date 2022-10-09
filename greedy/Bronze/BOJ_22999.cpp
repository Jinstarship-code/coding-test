#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int t;
	cin >> t;
	int cnt = 1;
	vector<int> result;

	while (t--)
	{
		int n, k;
		cin >> n >> k;
		string str;
		cin >> str;
		n--;

		int score = 0;
		int match_cnt = 0;
		for (int i = 0; i <=n/2 ; ++i)
		{
			if (i == n - i)
				break;

			if (str[i] != str[n - i])
				score++;
			else
				match_cnt++;
		}

		if (score == k) 
			result.push_back(0);
		else 
			result.push_back(abs(k - score));

	}

	for (int i = 0; i < result.size(); ++i)
	{
		cout << "Case #" << i+1 << ": " << result[i]<<'\n';
	}

	return 0;
}