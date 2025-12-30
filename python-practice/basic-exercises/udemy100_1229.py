# 問題24
# 入力した英単語の中央に、@を差し込んで出力するプログラムを作成してください。
# なお、入力した英単語の長さが奇数なら、真ん中のアルファベットを@に変換してください。
# ```

# ●英単語の長さが偶数の場合
# ```
# 英単語を入力してください > Python
# 変換した英単語 : Pyt@hon
# ```

# ●英単語の長さが奇数の場合
# ```
# 英単語を入力してください > PHP
# 変換した英単語 : P@P
# ```

# 設計メモ
# ※偶数判定は「文字数を2で割った余りが0」であることとする
# ※文字列の真ん中をどうやって特定する？
# 　→　偶数：len()で取得した文字列の長さを2で割ると、真ん中のインデックスがわかる
# 　→　奇数：len()で取得した文字列の長さを2で割って小数点以下を切り捨てると、真ん中のインデックスがわかる
# ※＠を文字列に差し込むには？　→ 検索したら、スライスと文字列連結演算子を使用することで可能だった
# ※文字列の真ん中の文字を＠に置換するには？　→　replace()で真ん中のインデックスを指定して置換する
# 　追記修正：replace()ではインデックス指定不可だったため、奇数の場合もスライスと文字連結演算子を使用する
# ```
# inputで「英単語を入力してください > 」、受け取った文字列を変数Wordに格納
# Wordの長さを2で割り、計算結果を小数点以下切り捨て（ググったらintでOKみたい）て変数midに格納
# もし、Wordの長さを2で割ったときの余りが0なら、
# 　【「Wordの先頭からmid-1まで」＋「@」＋「Wordのmidから末尾まで」】を計算し、変数result_strに格納　●「mid-1まで」じゃなくて「midまで」だった
# それ以外の場合、
# 　【「Wordの先頭からmid-1まで」＋「@」＋「Wordのmid＋1から末尾まで」】を計算し、変数result_strに格納
# 「変換した英単語 : 」とresult_strをprintで出力

word = input("英単語を入力してください > ")
mid = int(len(word) / 2)
if len(word) % 2 == 0:
    result_str = word[:mid] + "@" + word[mid:]    # 当初、word[:mid-1] + "@" + word[mid:]にしてズレた 
else:
    result_str = word[:mid - 1] + "@" + word[mid + 1:]
print(f'変換した英単語 : {result_str}')    # @P　不正解！

# 再チャレンジ
word = input("英単語を入力してください > ")
mid = len(word) // 2    # 元々「int(len(word) / 2)」と書いていたのを修正
if len(word) % 2 == 0:
    result_str = word[:mid] + "@" + word[mid:]
else:
    result_str = word[:mid] + "@" + word[mid + 1:]
print(f'変換した英単語 : {result_str}')   

print("-" * 20)# ----------
# 問題25
# 入力した3つの英単語を、カンマ区切りでアルファベット順になるように並び替えるプログラムを作成してください。
# ```
# 1つ目の英単語を入力してください > Python
# 2つ目の英単語を入力してください > Ruby
# 3つ目の英単語を入力してください > Java
# 並び替えた英単語 : Java, Python, Ruby
# ```

# 設計メモ
# ※出力結果はリストではないけど、いったんリスト化したほうが並べ替えしやすそう
# ※検索したところ、リストをアルファベット順に並べ替えるにはsort()メソッドが使える
# ※検索したところ、「リストをカンマ+半角スペース」区切りの文字列に変換するにはjoin()メソッドが使える
# ```
# inputで「1つ目の英単語を入力してください > 」、受け取った文字列を変数word_1に格納
# inputで「2つ目の英単語を入力してください > 」、受け取った文字列を変数word_2に格納
# inputで「3つ目の英単語を入力してください > 」、受け取った文字列を変数word_3に格納
# word_1、word_2、word_3を格納したリストword_listを宣言
# word_listをsort()メソッドでアルファベット順に並べ替えたものをword_listに格納しなおす
# word_listをjoin()メソッドで「カンマ+半角スペース」区切りの文字列に変換し、変数word_strに格納
# 「並び替えた英単語 : 」とword_strをprintで出力

word_1 = input("1つ目の英単語を入力してください > ")
word_2 = input("2つ目の英単語を入力してください > ")
word_3 = input("3つ目の英単語を入力してください > ")
word_list = [word_1, word_2, word_3]
word_list = word_list.sort()    # 下記の原因はsort()メソッド！リファレンスをちゃんと読んだら「戻り値はNone」だった
word_str = ", ".join(word_list)    # ここで、word_listが「反復可能なオブジェクト（つまりリストなど）」になってない！とエラーが出た
print(f'並び替えた英単語 : {word_str}')

# 再チャレンジ
word_1 = input("1つ目の英単語を入力してください > ")
word_2 = input("2つ目の英単語を入力してください > ")
word_3 = input("3つ目の英単語を入力してください > ")
word_list = [word_1, word_2, word_3]
word_list = sorted(word_list)    # sort()メソッドではなくsorted()関数を使ってアルファベット順に並べ替えたリストを受け取り、word_listに格納しなおす
word_str = ", ".join(word_list) 
print(f'並び替えた英単語 : {word_str}')    # Java, Python, Ruby　正解

# もっとスマートなコード　入力が増えても対応できるように…
# ```
# 設計メモ
# 空のリストword_listを宣言
# for文のrange()を3回まわし、取り出した数をiに格納
# input()の、"「i+1」つ目の英単語を入力してください > "で受け取った英単語をword_listに要素として追加する
# ループが終わったら、word_listをsorted()関数でアルファベット順に並べ替えたものをword_listに格納しなおす
# word_listをjoin()メソッドで「カンマ+半角スペース」区切りの文字列に変換し、変数word_strに格納
# 「並び替えた英単語 : 」とword_strをprintで出力

word_list = []
for i in range(3):
    word_list.append(input(f'{i + 1}つ目の英単語を入力してください > '))
word_list = sorted(word_list)
word_str = ", ".join(word_list)
print(f'並び替えた英単語 : {word_str}')    # Java, Python, Ruby　正解

# sort()メソッドのコード1（私の解答：不正解）
word_list = []
for i in range(3):
    word_list.append(input(f'{i + 1}つ目の英単語を入力してください > '))
word_list = word_list.sort()    # 「word_list = 」でリストをsort()の戻り値で上書きするとNoneになってしまう
print(word_list)    # この行は実験用　None
word_str = ", ".join(word_list)    # TypeError: can only join an iterable
print(f'並び替えた英単語 : {word_str}')    

# sort()メソッドのコード2（模範解答）
word_list = []
for i in range(3):
    word_list.append(input(f'{i + 1}つ目の英単語を入力してください > '))
word_list.sort()    # リストをsort()の戻り値で上書きせず、並び替えただけにする
print(word_list)    # この行は実験用　['Java', 'Python', 'Ruby']
word_str = ", ".join(word_list)    # エラーなし
print(f'並び替えた英単語 : {word_str}')    # 並び替えた英単語 : Java, Python, Ruby　●正解

print("-" * 20)# ----------
print("-" * 20)# ----------
# セクション5　リスト型
# 問題26
# リスト`[1, 2, 3, 4, 5]`に格納されている数値を足し合わせるプログラムを作成してください。
# ※組み込み関数を使わずに解いてみてください。
# ```
# リスト内の合計 : 15
# ```

# 設計メモ
# ※forループでリストの要素を1つずつ取り出して、前回計算した分と足し合わせていくことにする
# ```
# [1, 2, 3, 4, 5]を要素とするリストnum_listを宣言
# 変数resultを0で初期化して宣言
# for文でnum_listの要素を1つずつ取り出し、変数iに格納
# resultに、「result+i」を格納しなおす
# ループを抜けた後、「リスト内の合計 : 」とresultをprintで出力

num_list = [1, 2, 3, 4, 5]
result = 0
for i in num_list:
    result += i
print(f'リスト内の合計 : {result}')

print("-" * 20)# ----------
# 問題27
# 組み込み関数を使って、リスト`[1, 2, 3, 4, 5]`に格納されている数値を足し合わせるプログラムを作成してください。
# ```
# リスト内の合計 : 15
# ```

# 設計メモ
# ※検索したところ、リストの要素を簡単に合計するにはsum関数が使えるようだ
# [1, 2, 3, 4, 5]を要素とするリストlを宣言
# sum関数を用いてlの要素の合計を計算し、変数totalに格納する
# 「リスト内の合計 : 」とtotalをprintで出力

# コード1　私の解答　◎
l = [1, 2, 3, 4, 5]
total = sum(l)
print(f"リスト内の合計 : {total}")

# コード2　模範解答（2行で書くなら）△実務では「後で条件分岐・再利用する可能性が少しでもある値は変数にする」が常識。コード1のほうが良い！
l = [1, 2, 3, 4, 5]
print(f"リスト内の合計 : {sum(l)}")



print("-" * 20)# ----------
# 問題28

print("-" * 20)# ----------
# 問題29