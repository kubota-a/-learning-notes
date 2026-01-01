# 問題23　△
# 設計メモ
# ※出力はリスト型になっている　→　1つ目の英文・2つ目の英文をリスト化し、1つ目の英文をforループでまわし、重複判定して該当すれば空のリストに追加していく
# ※半角スペース区切りの文字列をリストに変換する　split()メソッドを使用
# ```
# 空のリストduplicate_sを宣言
# input()関数で「1つ目の英文を入力してください > 」、受け取った文字列をsplit()メソッドでリスト化したものを変数s1に格納
# input()関数で「2つ目の英文を入力してください > 」、受け取った文字列をsplit()メソッドでリスト化したものを変数s2に格納
# for文でs1の英単語を1つずつ取り出し、変数iに格納
# もしiがs2に含まれるなら、duplicate_sにiを要素として追加
# ループ終了後、「重複する英単語 : 」とduplicate_charsをprintで出力

duplicate_s = []
s1 = input("1つ目の英文を入力してください > ").replace(".", "")    # 「.」消すのを忘れていた
s2 = input("2つ目の英文を入力してください > ").replace(".", "")
s1 = s1.split()
s2 = s2.split()

for i in s1:
    if i in s2 and i not in duplicate_s:
        duplicate_s.append(i)
print(f'重複する英単語 : {duplicate_s}')

print("-" * 20)# ----------
# 問題24　△
# 設計メモ
# ※replace()ではインデックス指定での置換ができないため、不特定の文字列の置換には向かない。よってスライスと足し算で対応する
# ※文字数が偶数かどうかは÷2をした余りが0かどうかで判定する
# ```
# input()関数で「英単語を入力してください > 」、受け取った文字列を変数 word に格納
# もしwordの長さを÷2をした余りが0なら、
# 　「wordの先頭からwordの長さを÷2したインデックスまで」と「@」と「wordの、wordの長さを÷2したインデックスから末尾まで」を足し算して、変数resultに格納
# それ以外の場合、
# 　「wordの先頭からwordの長さを÷2したインデックスまで」と「@」と「wordの、wordの長さを÷2したインデックス+1から末尾まで」を足し算して、変数resultに格納
# 「変換した英単語 : 」と result をprintで出力

word = input("英単語を入力してください > ")
index = len(word) // 2
if len(word) % 2 == 0:
    result = word[:index] + "@" + word[index:]
else:
    result = word[:index] + "@" + word[index + 1:]
print(f'変換した英単語 : {result}')

print("-" * 20)# ----------
# 問題25
# 設計メモ
# ※文字列をアルファベット順に並べ替える　sortメソッド（元データが壊れる）かsorted関数（元データ保持）。今回はsortで行く
# ※sortメソッドはリストのメソッドなので、文字列をいったんリストに変換し、出力前に文字列に戻す
# ※「〇つ目の英単語を入力してください > 」が3連続するのを、forループとrange()で簡潔に書きたい　データの増加に対応しやすく！
# ```
# for文でrange(3)から「0,1,2」と1つずつ数を取り出し、変数iに格納
# input()関数で「{i+1}つ目の英単語を入力してください > 」、受け取った文字列をリストに変数wordに格納
# ×変数名で詰んだのでいったん中止

# 設計メモ2　△
# 空のリストword_listを宣言
# input()関数で「1つ目の英単語を入力してください > 」、受け取った文字列をword_listに追加
# input()関数で「2つ目の英単語を入力してください > 」、受け取った文字列をword_listに追加
# input()関数で「3つ目の英単語を入力してください > 」、受け取った文字列をword_listに追加
# word_listをsortメソッドでアルファベット順に並べ替える
# word_listをjoinメソッドでカンマ区切りのリストに変換してwordsに格納
# 「並び替えた英単語 : 」とwordsをprintで出力

word_list = []    # いらない！　単に、input()の戻り値を要素とするリストを作成すればよいだけ！
word_list.append(input("1つ目の英単語を入力してください > "))    # appendいらない
word_list.append(input("2つ目の英単語を入力してください > "))
word_list.append(input("3つ目の英単語を入力してください > "))
word_list.sort()
words = ", ".join(word_list)
print(f'並び替えた英単語 : {words}')

# データ増えてもいけるバージョンのリベンジ

# 空のリストword_listを宣言
# for文でrange(3)から「0,1,2」と1つずつ数を取り出し、変数iに格納
# input()関数で「{i+1}つ目の英単語を入力してください > 」、受け取った文字列をword_listに追加
# ループ終了後、word_listをsort()メソッドでアルファベット順に並べ替える
# word_listをjoinメソッドでカンマ+半角スペース区切りの文字列に変換し、変数wordsに格納
# 「並び替えた英単語 : 」とwordsをprintで出力

word_list = []
for i in range(3):
    word_list.append(input(f'{i+1}つ目の英単語を入力してください > '))
word_list.sort()
words = ", ".join(word_list)
print(f'並び替えた英単語 : {words}')