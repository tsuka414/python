s = input().strip().split(" ")  # アイテム数N、プレイ人数M、ランキング順位K
n1 = list(map(int, s))  # 数値変換

s = input().strip().split(" ")  # 得点Ci
n2 = list(map(float, s))  # 数値変換

score = [0 for i in range(n1[1])]  # 人数分の成績

for i in range(n1[1]):  # 一人ずつ設定
    s = input().strip().split(" ")  # 所持数Xi
    n3 = list(map(int, s))  # 数値変換

    for j in range(n1[0]):
        score[i] += n2[j] * n3[j]

score.sort()
score.reverse()

for i in range(n1[2]):
    print(int(score[i] + 0.5))  # python3 の round のアレにハマる。
