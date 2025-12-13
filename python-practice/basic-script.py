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

# 2025/12/09

# 制御構文 =====================================

# 問題：変数xが0より小さかったら「ゼロより小さいです」と表示する
x  = 0
if x < 0:
    print("ゼロより小さいです")
elif x > 0:    # elifの判定順序　1.if条件に合致しない場合は、2.elif条件に合致するか判定する　▶ ifが優先！
    print("ゼロより大きいです")
else:    # 条件に当てはまらない場合の動作を指定する
    print("これはゼロです！")

# 問題：変数xと変数yが、両方とも0より大きかったら「2つともゼロより大きいです」と表示する
x = 1
y = -2
if x > 0 and y > 0:    # ～かつ～
    print("2つともゼロより大きいです")

# 問題：変数xまたは変数yが、0より大きかったら「1つだけゼロより大きいです」と表示する
if x > 0 or y > 0:    # ～または～
    print("1つだけゼロより大きいです")
print("-" * 20)

# 演習問題4　
# 3で割り切れるときはFizz　
# 5で割り切れるときはBuzz　
# 3と5の両方で割り切れるときはFizzBuzz　
# いずれにも該当しない場合は、その数字を出力する
x = 15

# 下記の出力は「Fizz」になる
if x % 3 == 0:
    print("Fizz")
elif x % 5 == 0:
    print("Buzz")
elif x % 3 == 0 and x % 5 == 0:
    print("FizzBuzz")
else:
    print(x)

print("-" * 20)# ----------

# 下記の出力は「Fizz Buzz FizzBuzz」になる
if x % 3 == 0:
    print("Fizz")
if x % 5 == 0:
    print("Buzz")
if x % 3 == 0 and x % 5 == 0:
    print("FizzBuzz")
else:
    print(x)

print("-" * 20)# ----------

# 下記の出力は「FizzBuzz」になる。これが正解
# 「3と5の両方で割り切れる」を1番上に持ってくる
if x % 3 == 0 and x % 5 == 0:
    print("FizzBuzz")
elif x % 3 == 0:
    print("Fizz")
elif x % 5 == 0:
    print("Buzz")
else:
    print(x)

print("-" * 20)# ----------

# もっと簡潔に
if x % 15 == 0:
    print("FizzBuzz")
elif x % 3 == 0:
    print("Fizz")
elif x % 5 == 0:
    print("Buzz")
else:
    print(x)

print("-" * 20)# ----------

# ----------------
# セイウチ演算子 :=

# もし3文字以上の文字列だったら、その長さを出力する
y = "あいうえお"
if len(y) >= 3:
    print(len(y))

print("-" * 20)# ----------

if (n := len(y)) >= 3:
    print(n)

# ----------------
# forループ　繰り返し処理したい対象があって、それをループ

# 問題：数字の0～4を出力する
print("-" * 20)# ----------

print(0)
print(1)
print(2)
print(3)
print(4)

print("-" * 20)# ----------

# range()　0からスタートして、「()内で指定した数字ー1のインデックスまで」の連続した数値を要素として持つ
    # ※後ろの数字指定は基本的に「1つ減る」と覚える
# range(3)　0～2
# range(5)　0～4
# 0からでなく1からスタートしたい場合は、range(5)ではなく、　range(1,5)

for i in range(5):    # (インデックスの数)
    print(i)    # 0 1 2 3 4

print("-" * 20)# ----------

for i in range(1,5):    # (開始インデックス,終了インデックス)
    print(i)    # 1 2 3 4

print("-" * 20)# ----------

for i in range(1,5,2):    # (開始インデックス,終了インデックス,スキップ幅)
    # スキップ幅「2」なら1つ飛ばし
    print(i)    # 1 3

print("-" * 20)# ----------

# 文字列のインデックスを指定して、1文字ずつ取り出して出力する△
word = "Python"
for i in range(6):    # "Python"が6文字だから(6)
    print(word[i])    # P y t h o n

print("-" * 20)# ----------

# 文字列のインデックスを指定して、1文字ずつ取り出して出力する〇
# もっとスマートに、汎用性高いコード
word = "Python"
for i in range(len(word)):
    print(word[i])    # P y t h o n

print("-" * 20)# ----------

# 文字列のインデックスを指定せずに1文字ずつ取り出して出力する◎
# ※これを始めに試して、だめならrange()使う。
word = "Python"
for s in word:    # 文字列を直接参照（＝文字列をループの対象に）してfor文を適用している
    print(s)    # P y t h o n

print("-" * 20)# ----------

# 12/11
# ----------------
# whileループ　単純にループ内の処理を繰り返す
# 問題：変数iに0を格納して、そのあと1を3回足し合わせて出力する

# for文の場合
i = 0
for i in range(3):
    x = i + 1
    if x >= 3:
        print(x)

print("-" * 20)# ----------
# 構文を使わない場合
i = 0
i = i + 1
i = i + 1 
i = i + 1
print(i)

print("-" * 20)# ----------
# while文の場合 「単純に処理を繰り返したいとき」※無限ループの危険あり
i = 0
while i < 100:    # 条件
    i = i + 1    # 処理内容
print(i)    # shile分から外れて次の処理

print("-" * 20)# ----------
# break文でループ処理を途中で中断する
# while文のループで数字の0から9を出力しているとき、変数iが5になったら中断したい
i = 0
while i < 10:    # 条件
    if i == 5:    # 停止条件
        break    # 停止（必ずif文とセット）
    i = i + 1    # 処理内容
    print(i)    # shile分から外れて次の処理

print("-" * 20)# ----------
# continue文でループ処理をスキップする
# 0から9までを出力するfor文ループで、数字が5になったら処理をスキップして
# 次のループに飛ばししたい
i = 0
for i in range(10):
    if i == 5:    # 処理をスキップする条件
        continue    # スキップ
    print(i)    # 5だけスキップして出力

print("-" * 20)# ----------
# 問題：0から9までを出力するfor文ループで、3の倍数のみ除外して出力
i = 0
for i in range(10):
    if i % 3 == 0:    # 処理をスキップする条件
        continue    # スキップ
    print(i)    # 3の倍数だけスキップして出力（124578）

print("-" * 20)# ----------

# データ構造 =====================================

# 以降はLoopに記載済み
# ----------------
# リスト（list）1つの変数の中に複数の値を入れるデータ型　「複数の値を扱いたい」
# 変数[要素1,要素2,要素3…]
numbers = [1, 2, 3, 4, 5]    # リストを定義
print(numbers)    # [1, 2, 3, 4, 5]  変数名だけ→全要素を出力
print(type(numbers))    # <class 'list'>  データ型は「リスト型」

print("-" * 20)# ----------
# 数字以外の要素も格納可能
# 変数languagesに、Python、Java、Golangを入れたリストを作成
languages = ["Python", "Java", "Golang"]
print(languages)

# 数字、文字列、bool値など、異なるデータ型の要素も一緒に格納可能
mix = [1, "Python", True, 33]

# 要素を個別に取り出す
print(mix[0])    # 1  要素のインデックスを指定する
print(mix[2])    # True  要素のインデックスを指定する

# 特定の要素をまとめて取り出す
# mixから1、"Python"。Trueを取り出す
# 文字列と同じようにスライスを使う
print(mix[0:2]) # [1, 'Python']　✖　
print(mix[0:3]) # [1, 'Python', True]　〇　スライスの終わりは終了インデックス+1

# 要素を1つずつ順番に取り出す
for i in range(len(mix)):    # mixの要素数分の数字が入った袋をrange()で作成
    print(mix[i])    # 1　Python　True　33　
# 各ループで該当するインデックスをmix[i]で指定してる

print("-" * 20)# ----------
# 文字列と同じように直接、要素を1つずつ順番に取り出す
# for i in mix:
#     print(mix[i]) 　
# ✖　ここでのiはインデックスじゃなくて要素そのものだから、mix[i]はNG
for i in mix:
    print(i)    # 1　Python　True　33 　〇

print("-" * 20)# ----------
# 以降、説明等はLoopに記載、ここでは実演のみ

# 変数はインデックス用のi・要素用のvを用意しておく
for i, v in enumerate(mix):
    print(i, v)
print("-" * 20)# ----------
print(1 in mix)    # True　
print(22 in mix)    # False
print("Python" in mix)    # True
print("Java" in mix)    # False

print("-" * 20)# ----------

mix = [1, "Python", True, 33]
mix[1] = "Java"
print(mix)

print("-" * 20)# ----------

num1 = [1, 2, 3, 4, 5]
num2 = [6, 7, 8, 9, 10]

print(num1 + num2)

print("-" * 20)# ----------
print(num1 * 2)
print("-" * 20)# ----------

# 演習5
num3 = [0]
print(num3 * 10)
print("-" * 20)# ----------

nums = [1, 2, 3, 4, 5]
nums.append(6)    # 要素「6」を追加
print(nums)    # [1, 2, 3, 4, 5, 6]

# 数字の0～4をforループで回して、各数字を2倍した値をリストに要素として格納したい。
nums = []
for i in range(5):
    nums.append(i * 2)    # numsに要素「i * 2」を追加
print(nums)    # [0, 2, 4, 6, 8]

num1 = [1, 2, 3, 4, 5]
num2 = [6, 7, 8, 9, 10]

num1.extend(num1)

print(num1)    # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]　
print(num2)    # [6, 7, 8, 9, 10]

print("-" * 20)# ----------

nums = [1, 2, 3, 4, 5, 3]

print(nums)    # [1, 2, 3, 4, 5, 3]
nums.remove(3)
print(nums)    # [1, 2, 4, 5, 3]
print("-" * 20)# ----------
nums4 = [] 
for i in range(5):
    nums4.append(i)
print(nums4)

print("-" * 20)# ----------
nums4 = [i for i in range(5)]
print(nums4)
print("-" * 20)# ----------
print("-" * 20)# ----------
# 変数numbersから10以上30未満の値だけを抽出したリストを、作成したい
numbers = [20, 58, 19, 4, 29, 31, 5, 1, 39, 13, 30]
new_numbers = []

for i in numbers:
    if 10 <= i < 30:    # iが10以上30未満なら
        new_numbers.append(i)    # new_numbersに要素iを追加する
print(new_numbers)    # [20, 19, 29, 13]

print("-" * 20)# ----------
# 内包表記バージョン
numbers = [20, 58, 19, 4, 29, 31, 5, 1, 39, 13, 30]
new_numbers = []

new_numbers = [n for n in numbers if 10 <= n < 30]    # [n + for文 + 条件]
print(new_numbers)    # [20, 19, 29, 13]

print("-" * 20)# ----------

fruits = {"apple": 100, "banana": 120}
print(fruits, type(fruits))

# Valueの取得
print(fruits["apple"])    # Keyを指定する　100
print(fruits["banana"])    # 120

# Valueの変更
fruits["apple"] = 150
print(fruits["apple"])    # 150

fruits["peach"] = 180    # 存在しないKeyを指定して値を代入する
print(fruits)

word2 = ["p", "y", "t"]
word2[0] = "b"    # []でインデックスを指定して新しい値を代入する
print(word2)    # ['b', 'y', 't']


print("-" * 20)# ----------
fruits = {"apple": 100, "banana": 120, "peach":150}
print(fruits)


# 辞書にはいっているKeyをすべて取得したい
print(fruits.keys())    # dict_keys(['apple', 'banana', 'peach'])
# .keys()の()は空白でOK！引数（外部からの情報提供）がなくても戻り値（辞書内のすべてのKey）を返せるから

# forループを使うと1つずつKeyを取り出せる
for key in fruits.keys():
    print(key)

print(fruits.values())    # dict_values([100, 120, 150])

for value in fruits.values():
    print(value)

print("-" * 20)# ----------

for key in fruits.keys():
    print(key, fruits[key])

print("-" * 20)# ----------
print(fruits.items()) 

for key, value in fruits.items():
    print(key, value)

print("-" * 20)# ----------

fruits = {"apple": 100, "banana": 120, "peach":150}
# Valueの取得
print(fruits["apple"])    # 100　直接Keyを指定して取得


# Valueの取得(getメソッド)
print(fruits.get("apple"))    # 100　直接Keyを指定しなくても取得できる
print(fruits.get("grape"))    # None 存在しないKeyを入れてもエラーにならない

print("-" * 20)# ----------

fruits = {"apple": 100, "banana": 120, "peach":150}
print(fruits)  # {'apple': 100, 'banana': 120, 'peach': 150}

fruits2 = {"apple": 100,"banana":100, "grape":250}
fruits.update(fruits2)    # fruitsをfruits2でアップデートする
print(fruits)  # {'apple': 100, 'banana': 100, 'peach': 150, 'grape': 250}

fruits = {"apple": 100, "banana": 120, "peach":150}
fruits.pop("apple")    # Key"apple"を指定して要素を削除
print(fruits)  # {'banana': 120, 'peach': 150}

fruits = {"apple": 100, "banana": 120, "peach":150}
del fruits["peach"]    # Key"peach"を指定して要素を削除
print(fruits)  # {'apple': 100, 'banana': 120}