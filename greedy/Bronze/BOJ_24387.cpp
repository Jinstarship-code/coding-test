#include <iostream>
#include <algorithm>

using namespace std;

long long a[3];
long long b[3];


long long result = 0;

int main()
{
	for (int i = 0; i < 3; ++i)
		cin >> a[i];
	for (int i = 0; i < 3; ++i)
		cin >> b[i];

	sort(a, a + 3);
	sort(b, b + 3);
	
	for (int i = 0; i < 3; ++i)
		result += a[i] * b[i];

	cout << result;
	


	return 0;
}
/*
	��. ��. �� 
	�� 1kg a1 BGN
	�� 1kg a2 BGN
	�� 1kg a3 BGN

	��� ���� b1,b2,b3
	������ �ո��� -> �ִ�ݾ�

	int �� ������ �Ѿ��
*/