from sys import *
import heapq
n = int(stdin.readline())
heap = []
for _ in range(n):
    data = int(stdin.readline())
    if data == 0 and heap:
        stdout.write(str(heapq.heappop(heap)[1])+'\n')
    elif data == 0 and not heap:
        stdout.write('0\n')
    else:
        heapq.heappush(heap,(-data, data))


