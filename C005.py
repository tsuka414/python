M = int(input())
for i in range(M):
    IP = input().strip().split('.')
    if len(IP) != 4:
        print('False')
        continue

    ans = 'True'
    for i in range(len(IP)):
        if IP[i].isdigit():
            n = int(IP[i])
            if n in range(0, 256):
                continue
            else:
                ans = 'False'
        else:
            ans = 'False'
    print(ans)
