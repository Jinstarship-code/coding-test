#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int n, k;
	cin >> n >> k;
	vector<float> a;

	for(int i=0;i<k;++i)
	{
		float tmp;
		cin >> tmp;
		a.push_back(tmp);
	}

	float sum = 0;
	float max = 0;

	if (n == k)
	{
		for (int i = 0; i < n; ++i)
		{
			sum += a[i];
		}
		cout << sum / (float)n << ' ' << sum / (float)n;
	}
	else
	{
		for (int i = 0; i < k; ++i)
		{
			sum += a[i];
			max += a[i];
		}
		sum += (n - k) * -3.0;
		max += (n - k) * 3.0;
		cout << sum/(float)n << ' '<<max/(float)n;

	}
	return 0;
}

/*
	n : 판단해야하는 문제 수
	k : 이미 판단된 문제 수
	r(-3 ~ 3) : 점수
*/