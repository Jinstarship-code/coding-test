#include <iostream>

using namespace std;

int n, m, x, y, dir;

int d[50][50];
int arr[50][50];

int dx[] = { -1,0,1,0 };
int dy[] = { 0,1,0,-1 };

void turn_left() {
	dir -= 1;
	if (dir == -1)
		dir = 3;
}

int main()
{
	cin >> n >> m;
	cin >> x >> y >> dir;

	d[x][y] = 1;

	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < m; ++j)
		{
			int x;
			cin >> x;
			arr[i][j] = x;
		}
	}

	int cnt = 1;
	int turn_time = 0;
	while (true)
	{
		turn_left();
		int nx = x + dx[dir];
		int ny = y + dy[dir];

		if (arr[nx][ny] == 0 && d[nx][ny] == 0)
		{
			d[nx][ny] = 1;
			x = nx;
			y = ny;
			cnt++;
			turn_time = 0;
			continue;
		}
		else
			turn_time++;

		if (turn_time == 4)
		{
			nx = x - dx[dir];
			ny = y * dy[dir];

			if (arr[nx][ny] == 0)
			{
				x = nx;
				y = ny;
			}
			else
				break;
			turn_time = 0;
		}
	}

	cout << cnt;


	return 0;
}