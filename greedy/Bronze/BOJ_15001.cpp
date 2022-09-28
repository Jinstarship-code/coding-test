#include <iostream>

using namespace std;

int main()
{
	int stop_num;
	cin >> stop_num;

	/*
		한번에 점프를 하면 할수록
		에너지 소비가 더큼
		따라서, 한칸한칸 점프가 에너지 효율이 좋음
	*/
	
	long long sum = 0;

	long long first_num;
	cin >> first_num;
	stop_num--;
	while (stop_num--)
	{
		long long tmp;
		cin >> tmp;
		sum += (tmp - first_num) * (tmp - first_num);
		first_num = tmp;
	}
	cout << sum;

	return 0;
}