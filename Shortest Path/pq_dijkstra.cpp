#include <bits/stdc++.h>
#define INF 1e9
using namespace std;

int n, m, start;
vector<pair<int, int>> graph[100001];

int d[100001];

// start = 1  (0,1) 뜻 , 1번 노드의 거리는 0
void dijkstra(int start)
{
	priority_queue<pair<int, int>> pq;
	pq.push({ 0,start });
	d[start] = 0;
	while (!pq.empty())
	{
		int dist = -pq.top().first;
		int now = pq.top().second;

		pq.pop();
		if (d[now] < dist)
			continue;
		for (int i = 0; i < graph[now].size(); ++i)
		{
			int cost = dist + graph[now][i].second;
			if (cost < d[graph[now][i].first])
			{
				d[graph[now][i].first] = cost;
				pq.push(make_pair(-cost, graph[now][i].first));
			}
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
		graph[a].push_back({ b,c });
	}

	fill(d, d + 100001, INF);

	dijkstra(start);

	for (int i = 1; i <= n; ++i)
	{
		if (d[i] == INF)
			cout << "Infinity\n";
		else
			cout << d[i] << '\n';
	}

	return 0;
}