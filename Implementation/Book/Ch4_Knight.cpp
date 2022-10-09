#include <iostream>
#include <string>
#include <vector>

using namespace std;

int dx[] = { -2,-1,1,2,2,1,-1,-2 };
int dy[] = { -1,-2,-2,-1,1,2,2,1 };

int main()
{
	string str;
	cin >> str;

	int row = str[1] - '0';
	int column = str[0] - 'a'+1;
	
	int cnt = 0;
	for (int i = 0; i < 8; ++i)
	{
		int next_row = row + dx[i];
		int next_column = column + dy[i];

		if (next_row >= 1 && next_row <= 8 && next_column >= 1 && next_column <= 8)
			cnt++;
	}

	cout << cnt;


	return 0;
}