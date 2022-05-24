from sys import *
import heapq

def dij(start):
    distances = {node: float('inf') for node in dijkstra}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start],start])
    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in dijkstra[current_destination]:
            distance = current_distance + new_distance
            if distance < distances[new_destination] :
                distances[new_destination] = distance
                heapq.heappush(queue,[distance,new_destination])

    return distances

n, m = map(int, stdin.readline().split())

while n != 0 and m != 0:
    state = [i for i in range(n)]
    s, d = map(int, stdin.readline().split())
    dijkstra = {i:[] for i in range(n+1)}
    for _ in range(m):
        u, v, p = map(int, stdin.readline().split())
        dijkstra[u] += [[v,p]]
    dij(s)


