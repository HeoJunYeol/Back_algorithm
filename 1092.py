from sys import *
n = int(stdin.readline())
weight = sorted(list(map(int, stdin.readline().strip().split())), reverse=True)
m = int(stdin.readline())
boxes = sorted(list(map(int, stdin.readline().strip().split())), reverse=True)

# 모든 박스를 옮길 수 없을 경우
if boxes[0] > weight[0]:
    print(-1)
    exit()

# 각 크레인이 옮겨야 하는 박스의 번호
positions = [0] * n
# 각 박스를 옮겼는지 확인
checked = [False] * m

result = 0
count = 0

while True:
    if count == len(boxes):
        break
    for i in range(n): # 모든 크레인에 대하여 각각 처리
        while positions[i] < len(boxes):
            # 아직 안 옮긴 박스 중에서, 옮길 수 있는 박스를 만날 때까지 반복
            if not checked[positions[i]] and weight[i] >= boxes[positions[i]]:
                checked[positions[i]] = True
                positions[i] += 1
                count += 1
                break
            positions[i] += 1
    result += 1

print(result)