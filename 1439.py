from sys import *
string = stdin.readline().strip()
zero = 0 # 0으로 바꾸는 경우
one = 0 # 1로 바꾸는 경우

if string[0] == '1':
    zero += 1
else:
    one += 1

for i in range(len(string)-1):
    if string[i] != string[i+1]:
        if string[i+1] == '1':
            zero += 1
        else:
            one += 1

print(min(zero, one))
