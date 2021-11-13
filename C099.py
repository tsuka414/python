n, a = map(int, input().split())
list = [int(input()) for i in range(n-1)]

len = a

for i in range(n-1):
    len += a - list[i]

print(a*len)