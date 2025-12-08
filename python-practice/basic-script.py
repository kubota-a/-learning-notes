# 2025/12/07

print("こんにちは！")

# 演習問題　
# 変数aには3、変数bには-6が格納されています。
# 変数plus、minus、multiply、divideにaとbの足し算、引き算、掛け算、割り算の計算結果を格納して、すべて表示してください。
a = 3
b = -6
# 変数plusに足し算の結果を格納
plus = a + b
# 変数minusに引き算の結果を格納
minus = a - b
# 変数multiplyに掛け算の結果を格納
multiply = a * b
# 変数divideに割り算の結果を格納
divide = a / b
# 各計算結果の表示
print (plus, minus, multiply, divide) 

# 2025/12/08

# 文字列 =====================================

s = "Python"
print(s)
# 文字列とインデックス
print(s[0])
print(s[5])
# ”Pyt”を表示
print(s[0:3])    # [開始インデクス:終了インデックス+1]になる。[0:2]じゃなくて[0:3]！
print(s[:3])    # 0スタートなので開始インデックスを省略できる → 3まですべて取得
print(s[1:])    # 最後までなので終了インデックス+1を省略できる → 1からすべて取得
# "n"を表示
print(s[5])
# マイナス方向からインデックスを指定する
s = "fjeophslgotnnoremcl"
print(s[-1]) # 末尾の"l"を表示
print(s[-2]) # 末尾から2番目の”c”を表示
# 文字列の長さを知りたい
print(len(s))

# 文字列の演算
print("Mr." + "Children")    # Mr.Children

s = "A"
print(s * 3)    # AAA
# 区切り線が作れる
print("="*10, "足し算", "="*10)    # ========== 足し算 ==========
print(13 + 17)                     # 30 
print("="*10, "掛け算", "="*10)    # ========== 掛け算 ==========
print(13 * 17)                     # 221

# 文字列のメソッド

# ●.index()  ある文字列のなかの特定のインデックスを調べたい
s = "Python"
print(s.index("t"))    # 2  文字列Pythonの"t"のインデックスは2
print(s.index("ho"))    # 3  文字列Pythonの"ho"のインデックスは3

# ●.find()  ある文字列のなかに特定の文字が存在するかどうかを確認して、存在するならそのインデックスを調べたい
print(s.find("a"))    # -1　存在しない文字列を指定すると-1を返す
print(s.find("t"))    # 2　文字列Pythonに"t"は存在し、そのインデックスは2

# ●.replace(置換対象の文字,置換したい文字)  文字列の置換　
# ※文字列以外のデータに実行するとエラーになる
print(s.replace("on", "off"))    # Pythoff  文字列Pythonの"on"の文字を"off"に変えたい
# 文字列の削除にも使える .replace(置換対象の文字,空白)
price = "1,744円"
print(price.replace(",", "").replace("円", ""))    # 1744  "1,744円"からカンマと円を削除

# bool値と比較演算子 =====================================
# 比較演算子
a = 3
# ●==　両者は等しい？
print(a == 3)    # True  aは3と等しくない
print(a == 2)    # False  aは3と等しくない

# ●!=　aは3と等しくない？
print(a != 3)    # False  aは3と等しい

# ●>=　「大なりイコール」　aは3以上？
print(a >= 3)    # True  aは3以上

# ●>　aは3より大きい？
print(a > 3)   # False  aは3より大きくない

# ●<　「小なり」　aは3より小さい？
print(a < 3)   # False  aは3より小さくない

# ●<=　aは3以下？
print(a <= 3)    # True  aは3以下
# ----------------
# 文字列にも　比較演算子のような役割を持つ文法がある

# ●in　文字列を含むかどうかを判定する(大文字小文字区別あり)
print("P" in "Python")  # True  存在する

# ●in　”p”は文字列”Python”の中に存在しない？
print("p" not in "Python")    # True　存在しない

# ----------------
# ●～and～  条件の複数化
a = 3
# aが2より大きく、10以下かどうかを判定
print(a > 2 and a < 10)    # True  aは2より大きく、10以下である

# もっと良い書き方 ▶ aが2より大きく、10以下かどうかを判定
# aを挟む形で大小関係を確認するときは、aを真ん中に置く
print(2 < a <= 10)    # True  aは2より大きく、10以下である

# データ型とキャスト =====================================
# ●type()　データ型の判定
a = 2
print(type(a))    # int　整数型

six = 6
print(type(six))    # int　整数型

pi = 3.14
print(type(pi))    # float  小数（実数）型　double型

text = "テキスト"
print(type(text))    # str　ストリング型　→文字列

is_ok = True
print(type(is_ok))    # bool  bool型

# ----------------
# キャスト（型変換）
three = 3
# ●変数threeを文字列に変換●
# 1. 変数threeの中身と、そのデータ型を表示
print(three, type(three))    # 3 <class 'int'>　中身は3、データ型はint型
# 2. 変換後の値を入れる変数three_strの中に、「str(three)」
three_str = str(three)    # 変数threeを文字列に変換
print(three_str, type(three_str))    # 3 <class 'str'>　中身は3、データ型はストリング型

# 変数three_strをint型に変換(変換する▶キャストする)
three_int = int(three_str)
print(three_int, type(three_int))    # 3 <class 'int'>　中身は3、データ型はint型

# 変数threeと変数three_strが等しいか判定
print(three == "three_str")    # False　見た目はどちらも「3」だけど等しくない。
# 変数threeと変数three_intが等しいか判定
print(three == three_int)    # True　等しい。どちらも整数の3

# ※いったんfloat型からint型に変換した数値は、元のfloat型に戻すことはできない
tow_point_nine = 2.9
tow_point_nine_int = int(tow_point_nine)
print(tow_point_nine_int, type(tow_point_nine_int))    # 2 <class 'int'> 

tow_point_nine_float = float(tow_point_nine_int)
print(tow_point_nine_float, type(tow_point_nine_float))    # 2.0 <class 'float'>

print(tow_point_nine == tow_point_nine_float)    # False　2.9と2.0で、別物になってしまった

# 演習3　
# 文字列1,980円を数値型1980にキャストしてください。
price_1980yen = "1,980円"
price_1980yen.replace(",", "").replace("円", "")    # ,や円は数値型に変換できないので、まず削除する
# ※変数price_1980yenの中身が1980に書き換えられたわけではない
print(price_1980yen)    # なので、これだと1,980円のまま。
print(price_1980yen.replace(",", "").replace("円", ""))    # これなら1980になる
# 「price_1980yen.replace(",", "").replace("円", "")」を整数型にキャストする
number_1980 = int(price_1980yen.replace(",", "").replace("円", ""))
print(number_1980, type(number_1980))    # 1980 <class 'int'>　int型の「1980」に変換された

# ----------------
# None（ナン） 何もないことを表す
x = None
print(x)    # None　と表示される
print(type(x))    # <class 'NoneType'>

# ●is　変数の中身がNoneであるかを判定する
print(x is None)    # True xの中身はNoneである
