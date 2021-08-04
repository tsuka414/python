s = input()

s2 = s.translate(str.maketrans({'0': 'C', '1': 'A', '2': 'B'}))

print(s2)