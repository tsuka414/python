l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']

print(l.count('a'))
# 4

print(l.count('b'))
# 1

print(l.count('c'))
# 2

print(l.count('d'))
# 0
 
list = list(int(input()) for i in range(7))

wa = sum(i <= 30 for i in list)

print(wa)


