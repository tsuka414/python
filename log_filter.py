n = int(input())
G = input()
words = [input() for i in range(n)]

i = 0

for judge in words:
    if G in judge:
        print(judge)
        i = i + 1

if i == 0:
    print("None")