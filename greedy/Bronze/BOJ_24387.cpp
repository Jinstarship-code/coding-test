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
	아. 린. 해 
	아 1kg a1 BGN
	린 1kg a2 BGN
	해 1kg a3 BGN

	용기 종류 b1,b2,b3
	섞으면 손모가지 -> 최대금액

	int 의 범위를 넘어간다
*/