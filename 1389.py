from sys import *
from collections import deque

n, m = map(int, stdin.readline().split())
adj = [[] for _ in range(n+1)]
result = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, stdin.readline().split())
    adj[a] += b
    adj[b] += a

