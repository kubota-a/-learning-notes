# 設計メモ
# ※
# ```
# input()関数で「1つ目の文字列を入力してください > 」、受け取った文字列を変数wordsに格納
# ループ終了後、「重複する文字列 : 」とduplicate_charsをprintで出力




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