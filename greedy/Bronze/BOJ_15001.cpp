#include <iostream>

using namespace std;

int main()
{
	int stop_num;
	cin >> stop_num;

	/*
		�ѹ��� ������ �ϸ� �Ҽ���
		������ �Һ� ��ŭ
		����, ��ĭ��ĭ ������ ������ ȿ���� ����
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