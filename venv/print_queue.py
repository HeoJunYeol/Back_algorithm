from collections import deque
def solution(queue1, queue2):
    answer = 0
    state = False
    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    if (queue1_sum + queue2_sum) % 2 != 0:
        answer = -1
        return answer
    for _ in range(len(queue1)*5):
        if queue1_sum > queue2_sum:
            data = queue1.popleft()
            queue1_sum -= data
            queue2_sum += data
            queue2.append(data)
            answer += 1
        elif queue1_sum < queue2_sum:
            data = queue2.popleft()
            queue1_sum += data
            queue2_sum -= data
            queue1.append(data)
            answer += 1
        elif queue1_sum == queue2_sum:
            state = True
            break
    if state == True:
        return answer
    else:
        answer = -1
        return answer


queue1 = [1,1]
queue2 = [1,5]

print(solution(queue1,queue2))