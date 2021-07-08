# translate()メソッド
text = 'Python Programming'
m = {'a':'@',  'i':'1', 'o':'0', 't':'+'}

t = text.translate(str.maketrans(m))
print(t)