# 問題23
# 2つの文字列を入力して、重複する「英単語」を出力するプログラムを作成してください。
# ※少し難しいですが、出力の形に注目すると、答えが見えてくるはずです。
# ```
# 1つ目の英文を入力してください > Python is hard.
# 2つ目の英文を入力してください > PHP is easy.
# 重複する英単語 : ['is']
# ```

# 設計メモ
# ※出力されているのは「リスト」である
# ※どうすれば半角スペースで区切られた英単語を1つのかたまりとして扱えるか？
# ※　→　英単語をリストなどの要素にしたい　→　「半角スペース　区切り」で検索したらsplit()メソッドがヒットしたのでこれを使用する！
# ※英文の末尾のピリオドごとリスト化されてしまったため、まずピリオドをreplace()で空白に置換する
# ```
# 空のリストduplicate_wordsを宣言
# inputで「1つ目の英文を入力してください > 」、受け取った英文のピリオドをreplace()で空白に置換し、変数str_1に格納
# str_1を、split()によって空白区切りでリスト化する
# inputで「2つ目の英文を入力してください > 」、受け取った英文のピリオドをreplace()で空白に置換し、変数str_2に格納
# str_2を、split()によって空白区切りでリスト化する
# for文でstr_1の英単語を1つずつ取り出し、変数iに格納
# もしiがstr_2に含まれる場合は、duplicate_wordsにiを要素として追加
# ループが終わったら、「重複する英単語 : 」とduplicate_wordsをprintで出力

duplicate_words = []

str_1 = input("1つ目の英文を入力してください > ").replace(".", "")
str_1 = str_1.split()
str_2 = input("2つ目の英文を入力してください > ").replace(".", "")
str_2 = str_2.split()

for i in str_1:
    if i in str_2:
        duplicate_words.append(i)
print(f'重複する英単語 : {duplicate_words}')

# ※重複する単語が「各1回ずつ」のみduplicate_wordsに追加されるように修正
# for文の条件部分の修正　→　もしiがstr_2に含まれていて、かつ、duplicate_wordsに含まれていない場合は、
duplicate_words = []

str_1 = input("1つ目の英文を入力してください > ").replace(".", "")
str_1 = str_1.split()
str_2 = input("2つ目の英文を入力してください > ").replace(".", "")
str_2 = str_2.split()

for i in str_1:
    if i in str_2 and i not in duplicate_words:
        duplicate_words.append(i)
print(f'重複する英単語 : {duplicate_words}')

print("-" * 20)# ----------
# 問題24
# 