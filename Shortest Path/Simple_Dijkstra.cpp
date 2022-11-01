#include <bits/stdc++.h>
#define INF 1e9

using namespace std;

int n, m, start;
vector<pair<int, int>> graph[100001];

bool visited[100001];
int d[100001];

int getSmallestNode()
{
	int min_value = INF;
	int index = 0;
	for (int i = 1; i <= n; ++i)
	{
		if (d[i] < min_value && !visited[i])
		{
			min_value = d[i];
			index = i;
		}
	}
	return index;
}

void dijkstra(int start)
{
	d[start] = 0;
	visited[start] = true;
	for (int i = 0; i < graph[start].size(); ++i)
		d[graph[start][i].first] = graph[start][i].second;

	// 시작 노드를 제외한 전제 n-1 개의 노드에 대해 반복
	for (int i = 0; i < n - 1; ++i)
	{
		int now = getSmallestNode();
		visited[now] = true;
		for (int j = 0; j < graph[now].size(); ++j)
		{
			int cost = d[now] + graph[now][j].second;
			if (cost < d[graph[now][j].first])
				d[graph[now][j].first] = cost;
		}
	}
}

int main()
{
	cin >> n >> m >> start;
	
	for (int i = 0; i < m; ++i)
	{
		int a, b, c;
		cin >> a >> b >> c;
		// a 노드 -> b 노드(비용 c)
		graph[a].push_back({ b,c });
	}


	fill_n(d, 100001, INF);
	dijkstra(start);

	
	return 0;
}

/*
   n (노드), m(간선), start(시작점)

   노드와 간선을 받았을때 모든 노드를 거치면서 최소값을 얻는 간선을 따라 마지막 노드까지 순회함.

*/