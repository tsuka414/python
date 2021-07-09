from datetime import datetime 

# 今日の日付（例：20180904）
today = datetime.now().strftime("%Y%m%d") 

# 1. 連結演算子を使用
file_1 = "file_" + today + ".txt"

# 2. %構文を使用
file_2 = "file_%s.txt" % today

# 3. formatメソッドを使用
file_3 = "file_{}.txt".format(today)

# 結果はすべて同じ（例：file_20180904.txt）