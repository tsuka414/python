n = int(input())
list = list(map(str, input().split()))

s = []

for i in range(n):
    s.append(list[i][0])

print(''.join(s))