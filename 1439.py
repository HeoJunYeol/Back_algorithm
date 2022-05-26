from sys import *
string = stdin.readline().strip()
zero = 0
one = 0

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
