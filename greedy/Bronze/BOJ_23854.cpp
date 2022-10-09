#include <iostream>


using namespace std;

int main()
{
	long long a, b;
	cin >> a >> b;

	if (a == 0 && b == 0)
		cout << 0 << " " << 0 << " " << 0;
	else if (a != b && a < 3 && b < 3)
		cout << -1;
	else
	{
		int win_a = (int)(a/3);
		int win_b = (int)(b/3);
		int draw = (int)(a%3);
		
		if (a % 3 != b % 3)
			cout << -1;
		else
			cout << win_a << " " << draw << " " << win_b;
	}


	return 0;
}





/*
	매 경기.
		이긴팀 3점. 진팀 0점
		비기면 각팀 1점.
		
	경기 끝.  a:b (높은 점수 : 낮은점수)




*/