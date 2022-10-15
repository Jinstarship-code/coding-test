#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n, m;

int arr[8][8]; // 입력받은 맵
int temp[8][8]; // 벽설치한 맵

// 방향
int dx[] = { -1,0,1,0 };
int dy[] = { 0,1,0,-1 };

int res;

void virus(int x, int y)
{
	for (int i = 0; i < 4; ++i)
	{
		int nx = x + dx[i];
		int ny = y + dy[i];

		if (nx >= 0 && nx < n && ny >= 0 && ny < m) 
		{
			if (temp[nx][ny] == 0)
			{
				temp[nx][ny] = 2;
				virus(nx, ny);
			}
		}
	}
}

int getScore()
{
	int score=0;
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			if (temp[i][j] == 0)
				score++;

	return score;
}

void dfs(int count)
{
	if (count == 3)
	{
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				temp[i][j] = arr[i][j];
	
	
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < m; ++j)
			{
				if (temp[i][j] == 2)
					virus(i, j);
			}
		}

		res = max(res, getScore());
		return;
	
	}

	//울타리 설치
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < m; ++j)
		{
			if (arr[i][j] == 0)
			{
				arr[i][j] = 1;
				count++;
				dfs(count);
				count--;
				arr[i][j] = 0;
			}
		}
	}
}

int main()
{
	cin >> n >> m;

	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < m; ++j)
		{
			scanf("%1d", &arr[i][j]);
		}
	}

	dfs(0);
	cout << res;
	return 0;
}