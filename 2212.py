n = int(input())
k = int(input())
sensor = sorted(list(map(int, input().split())))
line = [0] * n
cnt = 1

for i in range(1,n):
    line[i-1] = sensor[i] - sensor[i-1]

while True:
    if cnt == k:
        break

    # 가장 긴 거리를 제거
    line[line.index(max(line))] = 0
    cnt += 1

print(sum(line))