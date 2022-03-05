import math

n = int(input())

sum = 0
for i in range(n):
    s = input().split(" ")
    d = str(s[0])
    n = int(s[1])

    if "3" in d:
        sum += math.floor(n / 100 * 3)
    elif "5" in d:
        sum += math.floor(n / 100 * 5)
    else:
        sum += math.floor(n / 100)

print(sum)