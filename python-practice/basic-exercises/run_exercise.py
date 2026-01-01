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