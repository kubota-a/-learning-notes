# 12/11
# Q1：0〜10 の数字を順番に出力しよう
for i in range(11):
    print(i)

print("-" * 15)    # ----------------
# Q2：2〜10 の偶数だけを出力しよう▲
for i in range(0, 11, 2):
    print(i)
print("-" * 15)    # ----------------
for i in range(11):
    if i % 2 == 0:
        print(i)

print("-" * 15)    # ----------------
# Q3：文字列 "Python" の各文字を1文字ずつ出力しよう▲
word = "Python"
for s in word:
    print(s)
print("-" * 15)    # ----------------
word = "Python"
for i in range(len(word)):
    print(word[i])

print("-" * 15)    # ----------------
# Q4：文字列 "Hello" の長さを出力しよう
s = "Hello"
print(len(s))

print("-" * 15)    # ----------------
# Q5：文字列 "fjeophslgotnnoremcl" の最後から3文字を出力しよう▲
s = "fjeophslgotnnoremcl"
print(s[-3:])

print("-" * 15)    # ----------------
# 12/13

# ⑴　偶数（2の倍数）だけを抜き出したリストを作成して出力せよ。
numbers = [3, 10, 7, 4, 9, 12, 15, 2]
# STEP1：for で取り出す i は何？　→　要素そのもの
# STEP2：偶数の条件は？　→　2で割り切れる・またはスライスで1つ飛ばし
# STEP3：どこに入れる？　→　新しい変数new_numbersに入れる
new_numbers = []
for i in numbers:
    if i % 2 == 0:    # もしiが2で割り切れるなら、
            new_numbers.append(i)
print(new_numbers)

print("-" * 15)    # ----------------

# ⑵　5文字以上の単語だけを抜き出したリストを作成して出力せよ。
words = ["cat", "elephant", "dog", "tiger", "bird", "lion"]
# STEP1：for で取り出す i は何？　→　要素そのもの
# STEP2：条件は？　→　len()が返した数が5以上の要素だけを抜き出す
# STEP3：どこに入れる？　→　新たな変数new_wordsに格納
new_words = []
for i in words:
     if len(i) >= 5:    # もしiの文字列の長さが5以上なら
          new_words.append(i)
print(new_words)

print("-" * 15)    # ----------------
# ⑶　70点以上だけを “合格者リスト” として作成して出力せよ。
scores = [55, 90, 72, 40, 88, 67, 30]
# STEP1：for で取り出す i は何？　→　要素そのもの
# STEP2：条件は？　→　70以上の要素だけを抜き出す
# STEP3：どこに入れる？　→　新たな変数pass_listに格納
pass_list = []
for i in scores:
     if i >= 70:
          pass_list.append(i)
print(pass_list)

print("-" * 15)    # ----------------

# 12/20
# Loopのまとめノートの目次だけ見ながら、0時までにできるだけ内容を思い出してみるの巻！

# 文字列　インデックスとスライス
text = "Python"
print(text[2])     # t
print("n" in text)    # True
print(text[2:5])    # tho 終わりのインデックスは+1になる

# 後ろからインデックス指定したスライス ✖間違えた
 # 出力したいのは「tho」
print(text[-2:-4])    # 空白 ✖
print(text[-4:-1])    # tho　〇　
# スライスは、前からでも後ろからでもインデックス番号が「小さいほうからスタート」して+1のインデックスで終わる！
