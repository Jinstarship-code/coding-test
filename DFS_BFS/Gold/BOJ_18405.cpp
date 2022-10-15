#include <iostream>
#include <vector>
#include <queue>


using namespace std;

class Virus {
public:
	int index;
	int second;
	int x;
	int y;
	Virus(int index, int second, int x, int y)
	{
		this->index = index;
		this->second = second;
		this->x = x;
		this->y = y;
	}


	bool operator <(Virus& other)
	{
		return this->index < other.index;
	}
};

int n, k;
int graph[200][200];

int dx[] = {-1,0,1, 0 };
int dy[] = { 0,1,0,-1 };

vector<Virus> viruses;


int main()
{
	cin >> n >> k;

	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < n; ++j)
		{
			cin >> graph[i][j];

			if (graph[i][j] != 0)
				viruses.push_back(Virus(graph[i][j], 0, i, j));
		}
	}

	sort(viruses.begin(), viruses.end());
	queue<Virus> q;
	for (int i = 0; i < viruses.size(); ++i)
		q.push(viruses[i]);


	int target_s, target_x, target_y;
	cin >> target_s >> target_x >> target_y;

	while (!q.empty())
	{
		Virus virus = q.front();
		q.pop();

		if (virus.second == target_s)
			break;

		for (int i = 0; i < 4; ++i)
		{
			int nx = virus.x + dx[i];
			int ny = virus.y + dy[i];

			if (0 <= nx && nx<n && 0 <= ny && ny<n)
			{
				if (graph[nx][ny] == 0)
				{
					graph[nx][ny] = virus.index;
					q.push(Virus(virus.index,virus.second + 1, nx, ny));
				}
			}
		}
	}

	cout << graph[target_x - 1][target_y - 1];
}



/*

	시간초과나는 코드

#include <iostream>

using namespace std;

int n,k,s,x,y;

int arr[200][200];
int tmp[200][200]; //변화를 담을 배열

// 방향
int dx[] = { 0,0,-1,1 };
int dy[] = { -1,1,0,0 };



void virus(int x, int y, int k)
{
	for (int i = 0; i < 4; ++i)
	{
		int nx = x + dx[i];
		int ny = y + dy[i];
	
		//유효범위 안에 있으면
		if (nx >= 0 && nx < n && ny >= 0 && ny < n)
		{
			//실행.
			if (arr[x][y] == k && tmp[nx][ny] == 0)
				tmp[nx][ny] = k;
		}
	}
	
}

void dfs(int s)
{
	
	for (int m = 1; m <= k; ++m)
	{
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < n; ++j)
			{
				if (tmp[i][j] == m)
				{
					virus(i, j, m);
				}
			}
		}
	}

	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j)
			arr[i][j] = tmp[i][j];
	
}

int main()
{
	cin >> n >> k;

	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < n; ++j)
		{
			cin >> arr[i][j];
			tmp[i][j] = arr[i][j];
		}
	}
	cin >> s >> x >> y;

	for(int i=s; i>0;--i)
		dfs(i);
	
	cout << arr[x - 1][y - 1];
	return 0;
}
*/