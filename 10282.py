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


for _ in range(t):
    n, d, c = map(int, stdin.readline().split())
    dijkstra = {i:[] for i in range(n+1)}
    for _ in range(d):
        a, b, s = map(int, stdin.readline().split())
        dijkstra[b] += [[a,s]]
    result = dij(c)
    keys = result.keys()
    count = 0
    max_value = -1
    for i in keys:
        if result[i] != float('inf'):
            count += 1
            if result[i] > max_value:
                max_value = result[i]

    print(count, max_value)






