# 要素の結合

# join() 関数は、文字列のリストを一つの文字列に結合することができます。
# また、結合する際には、区切り文字を指定することもできます。

list = ['A', 'B', 'C']

print(''.join(list))
# ABC

print(','.join(list))
# A,B,C

#  リストの要素に数値が含まれる場合、join() 関数で要素の結合すると TypeError 例外が発生します。
#  その場合、map() 関数を使用して数値を文字列に変換する方法があります。

list = ['A', 'B', 'C', 1, 2, 3]

map = map(str, list)
print(''.join(map))
# ABC123