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
# 問題25　△　データ増加対応別解　×
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

print("-" * 20)# ----------
# 復習終わり

# 問題32
# リスト`['Python', 'Ruby', 'PHP', 'JavaScript']`に格納されている文字列が短いものから順番に並べるプログラムを作成してください。
# ```
# 短い順に並び替えたリスト : ['PHP', 'Ruby', 'Python', 'JavaScript']
# ```

# 設計メモ
# ['Python', 'Ruby', 'PHP', 'JavaScript']を要素とするwordsを宣言
# 空のリストnew_wordsを宣言
# wordsの要素の中で1番短い文字列を先頭の要素であると仮定するため、変数m_wordに wordsのインデックス0に該当する要素を格納
# 下記のforループを、wordsの要素の数だけ繰り返す
# ↓
# for文でwordsの要素を1つずつ取り出し、変数wに格納
# もしwの文字列の長さが、m_wordの文字列の長さよりも短い場合は、m_wordをwに更新する
# ループ終了後、
# m_wordをnew_wordsに格納
# m_wordのインデックスを取得し、delでwordsから削除
# ↓
# 上記のforループをwordsの要素の数だけ繰り返し終わったら、
# 「短い順に並び替えたリスト : 」とnew_wordsをprintで出力

words = ['Python', 'Ruby', 'PHP', 'JavaScript']
new_words = []
m_word = words[0]    # これ、ここじゃない！

for _ in range(len(words)):
    m_word = words[0]    # 当初はこの1文がなくて、下記の2回目のループの「del words[words.index(m_word)]」でValueErrorが出た！
    for w in words:
        if len(w) < len(m_word):
            m_word = w
    new_words.append(m_word)
    del words[words.index(m_word)]
print(f'短い順に並び替えたリスト : {new_words}')

# 模範解答
words = ['Python', 'Ruby', 'PHP', 'JavaScript']
new_words = sorted(words, key=len)
print(f'短い順に並び替えたリスト : {new_words}')


print("-" * 20)# ----------
# 問題33
# 2つのリストで共通の文字列を格納したリストを出力するプログラムを作成してください。
# ※使用するリスト :
# ```
# l1 = ['Python', 'Ruby', 'PHP', 'JavaScript']
# l2 = ['Java', 'Ruby', 'Golang', 'Python', 'TypeScript']
# ```
# ▼期待する出力
# ```
# 共通する値を格納したリスト : ['Python', 'Ruby']
# ```

# 設計メモ
# ※l1をforループでまわして、要素1つずつl2に含まれているかを判定していくことにする
# ```
# 2つのリスト、l1とl2を宣言
# 空のリストduplicate_wordsを宣言
# for文でl1の要素を1つずつ取り出し、変数wに格納
# wがl2に含まれていて、かつ、wがduplicate_wordsに含まれない場合は、wを要素としてduplicate_wordsに追加
# ループ終了後、「共通する値を格納したリスト : 」とduplicate_wordsをprintで出力

l1 = ['Python', 'Ruby', 'PHP', 'JavaScript']
l2 = ['Java', 'Ruby', 'Golang', 'Python', 'TypeScript']
duplicate_words =[]
for w in l1:
    if w in l2 and w not in duplicate_words:
        duplicate_words.append(w)
print(f'共通する値を格納したリスト : {duplicate_words}')

# 上記をリスト内包表記で
l1 = ['Python', 'Ruby', 'PHP', 'JavaScript']
l2 = ['Java', 'Ruby', 'Golang', 'Python', 'TypeScript']
duplicate_words =[w for w in l1 if w in l2 and w not in duplicate_words]
# duplicate_words =[w for w in l1 if w in l2 and w not in duplicate_words]　はNG！内包表記では作成中のリストは登場できない。こうしたいなら1つ目の解答。

# 模範解答
l1 = ['Python', 'Ruby', 'PHP', 'JavaScript']
l2 = ['Java', 'Ruby', 'Golang', 'Python', 'TypeScript']
duplicate_words =[]
for w1 in l1:
    for w2 in l2:
        if w1 == w2 and w1 not in duplicate_words:
            duplicate_words.append(w1)
print(f'共通する値を格納したリスト : {duplicate_words}')

print("-" * 20)# ----------
# 問題34

print("-" * 20)# ----------
# 問題35