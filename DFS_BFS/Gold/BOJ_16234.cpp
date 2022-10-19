#include <bits/stdc++.h>

using namespace std;

int n, l, r;


int graph[50][50];
int unions[50][50];

int dx[] = {-1,0,1,0};
int dy[] = { 0,-1,0,1 };



int moving_count;

void process(int x, int y, int index)
{
	vector<pair<int, int>> united;
	united.push_back({ x, y });

	queue<pair<int, int>> q;
	q.push({ x,y });

	unions[x][y] = index;
	int sum = graph[x][y]; //연합의 전체인구수
	int cnt = 1; //국가수

	while (!q.empty())
	{
		int x = q.front().first;
		int y = q.front().second;

		q.pop();

		for (int i = 0; i < 4; ++i)
		{
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (0 <= nx && nx < n && 0 <= ny && ny < n && unions[nx][ny] == -1)
			{
				int gap = abs(graph[x][y] - graph[nx][ny]);
				if (l <= gap && gap <= r)
				{
					q.push({ nx,ny });
					unions[nx][ny] = index;
					sum += graph[nx][ny];
					cnt +=1;
					united.push_back({ nx,ny });
				}
			}
		}
	}

	for (int i = 0; i < united.size(); ++i)
	{
		int x = united[i].first;
		int y = united[i].second;

		graph[x][y] = sum / cnt;
	}
}


int main()
{
	cin >> n >> l >> r;

	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < n; ++j)
		{
			//각 땅의 인구 입력.
			cin >> graph[i][j];
		}
	}

	while (true)
	{
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
				unions[i][j] = -1;

		int index = 0;
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < n; ++j)
			{
				if (unions[i][j] == -1)
				{
					process(i, j, index);
					index +=1;
				}
			}
		}

		if (index == n * n)
			break;
		moving_count +=1;
	}

	cout << moving_count;
	return 0;
}