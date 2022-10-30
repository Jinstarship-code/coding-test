#include <bits/stdc++.h>

using namespace std;
int n;

int Factorial(int n)
{
	if (n < 2)
		return 1;

	return n * Factorial(n - 1);

}


int main()
{

	
	cin >> n;
	cout << Factorial(n);
	

	return 0;
}

/*
 11 22 33 44


*/