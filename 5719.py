from sys import *
import heapq
t = int(stdin.readline())

def dij(start):
    distances = {node: float('inf') for node in dijkstra}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start],start])
    while queue:
        current_distance, current_destnation = heapq.heappop(queue)

        if distances[current_destnation] < current_distance:
            continue

        for new_destination, new_distance in dijkstra[current_destnation]:
            distance = current_distance + new_distance
            if distance < distances[new_destination] :
                distances[new_destination] = distance
                heapq.heappush(queue,[distance,new_destination])

    return distances

for i in range(t):
    n, m = map(int, stdin.readline().split())
