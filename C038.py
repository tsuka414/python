n = input().strip().split(" ")
n = list(map(int, n))   # int変換

ans = [0, 1001, 1001]  # No, mod, q

for i in range(n[0]):
    a = int(input())
    m = n[1] % a
    q = n[1] // a

    if (m < ans[1])or (m == ans[1] and q < ans[2]):
        ans[0] = i + 1
        ans[1] = m
        ans[2] = q

print(ans[0])
