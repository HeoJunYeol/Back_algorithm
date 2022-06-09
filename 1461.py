import heapq
n, m = map(int, input().split())
location = list(map(int, input().split()))
positive = []
negative = []

# 가장 거리가 먼 책의 거리
largest = max(max(location), -min(location))

# 최대 힙으로 구현하기 위해 원소를 음수로 변경하여 push
for i in location:
    if i > 0:
        heapq.heappush(positive, -i)
    else:
        heapq.heappush(negative, i)

result = 0

while positive:
    result += heapq.heappop(positive)
    # 한번에 m개씩 옮길 수 있기 때문에 m개씩 빼내기
    for _ in range(m-1):
        if positive:
            heapq.heappop(positive)

while negative:
    result += heapq.heappop(negative)
    for _ in range(m-1):
        if negative:
            heapq.heappop(negative)

# 왕복거리를 계산하지만, 가장 먼 곳은 편도로 계산
print(-result * 2 - largest)