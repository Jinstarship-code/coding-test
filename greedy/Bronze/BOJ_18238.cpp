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
	- 그림과 같은 원판에 문자들이 순서대로 적혀있다. 처음 순간에 화살표는 'A'를 가리키고 있다.
	- 원판은 왼쪽 또는 오른쪽으로 돌릴 수 있다. 원판을 한 칸 돌리는 데에는 1의 시간이 소요된다.
	- 화살표가 가리키고 있는 문자를 출력할 수 있다. 문자를 출력하는 데에 걸리는 시간은 없다.

		
*/

