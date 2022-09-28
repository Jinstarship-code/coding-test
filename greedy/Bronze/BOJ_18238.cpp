#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	string str;
	cin >> str;

	int right = 0;
	int left = 0;
	char curLo = 'A';
	int sum = 0;
	for (int i = 0; i < str.size(); ++i)
	{
		right = abs(str[i] - curLo);
		left = 26 - right;
		sum += min(right, left);

		curLo = str[i];
	}
	cout << sum;
	return 0;
}

/*
	- �׸��� ���� ���ǿ� ���ڵ��� ������� �����ִ�. ó�� ������ ȭ��ǥ�� 'A'�� ����Ű�� �ִ�.
	- ������ ���� �Ǵ� ���������� ���� �� �ִ�. ������ �� ĭ ������ ������ 1�� �ð��� �ҿ�ȴ�.
	- ȭ��ǥ�� ����Ű�� �ִ� ���ڸ� ����� �� �ִ�. ���ڸ� ����ϴ� ���� �ɸ��� �ð��� ����.

		
*/

