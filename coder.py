# １行での入力
a, b, c = map(int, input().split())

# インプットされたものをint型に変換して変数ごとに代入。

# 複数行での入力 2行の場合
a = [int(input()) for i in range(2)]

def anti_vowel(text):
    vowels = ['a','e','i','o','u','A','I','U','E','O']
    new_text =[]
    for i in text:
        new_text.append(i)
        for j in vowels:
            if i == j:
                new_text.remove(j)
    return ''.join(new_text)
print anti_vowel('I am learning Python.')

# 重複を削除する
