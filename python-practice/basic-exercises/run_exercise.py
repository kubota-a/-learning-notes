# 設計メモ
# ※
# ```
# input()関数で「1つ目の文字列を入力してください > 」、受け取った文字列を変数wordsに格納
# ループ終了後、「重複する文字列 : 」とduplicate_charsをprintで出力


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

# 模範解答
l1 = ['Python', 'Ruby', 'PHP', 'JavaScript']
l2 = ['Java', 'Ruby', 'Golang', 'Python', 'TypeScript']
duplicate_words =[]
for w1 in l1:
    for w2 in l2:
        if w1 == w2 and w1 not in duplicate_words:
            duplicate_words.append(w1)
print(f'共通する値を格納したリスト : {duplicate_words}')