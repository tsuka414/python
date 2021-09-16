a = str(input())
b = str(input())

if a == b:
    print('NO')
elif set(a) == set(b):
    print('YES')
elif a != b:
    print('NO')