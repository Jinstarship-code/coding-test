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
	�� ���.
		�̱��� 3��. ���� 0��
		���� ���� 1��.
		
	��� ��.  a:b (���� ���� : ��������)




*/