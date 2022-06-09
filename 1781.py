import heapq
from sys import *
n = int(stdin.readline())
problem = []
heap = []

for _ in range(n):
    d, c = map(int, stdin.readline().strip().split())
    problem.append((d, c))
problem.sort()

for i in problem:
    a = i[0]
    heapq.heappush(heap, i[1])
    # 데드라인 초과 시 최소 원소 제거
    if a < len(heap):
        heapq.heappop(heap)


stdout.write(str(sum(heap)))