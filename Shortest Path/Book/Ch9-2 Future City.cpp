#include <bits/stdc++.h>
#define INF 1e9

using namespace std;

int n, m;

int graph[101][101];

int main()
{
	cin >> n >> m;

	for (int i = 0; i < 101; ++i)
	{
		fill(graph[i], graph[i] + 101, INF);
	}

	for (int a = 1; a <= n; ++a)
		for (int b = 1; b <= n; ++b)
			if (a == b)
				graph[a][b] = 0;

	for (int i = 0; i < m; ++i)
	{
		int a, b;
		cin >> a >> b;
		//¾ç¹æÇâ
		graph[a][b] = 1;
		graph[b][a] = 1;
	}

	int x, k;
	cin >> x >> k;

	for (int t = 1; t <= n; ++t)
		for (int a = 1; a <= n; ++a)
			for (int b = 1; b <= n; ++b)
				graph[a][b] = min(graph[a][b], graph[a][t] + graph[t][b]);
	
	int dist = graph[1][k] + graph[k][x];

	if (dist >= INF)
		cout << "-1";
	else
		cout << dist;


	return 0;
}