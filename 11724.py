from sys import *
from collections import deque
n, m = map(int, stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = 0

def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        data = queue.popleft()
        for idx in graph[data]:
            if not visited[idx]:
                visited[idx] = True
                queue.append(idx)


for _ in range(m):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        result += 1
print(result)