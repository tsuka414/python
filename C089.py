import itertools

a,b = map(int, input().split())

pp = [input().split() for l in range(a)]
oo = [input().split() for l in range(a)]

ii = (list(itertools.chain.from_iterable(pp)))
qq = (list(itertools.chain.from_iterable(oo)))

i = 0
uu = list()
for i in range(a):
    yy = list(ii[i])
    uu[len(uu):len(uu)] = yy
    i += 1
    
total = 0
i = 0

for i in range(a * b):
    if uu[i] == str('o'):
        total += int(qq[i])
    
print(total)