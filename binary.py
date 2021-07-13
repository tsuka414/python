# 2進数を10進数に変換
n = int(input())

print(int(f'{n}', 2))

# 10進数を2,8,16進数に変換する
x = 10
print(bin(x))
print(oct(x))
print(hex(x))

# 2,8,16進数を10進数に変換する
print(int('10100', 2))
print(int('24', 8))
print(int('14', 16))