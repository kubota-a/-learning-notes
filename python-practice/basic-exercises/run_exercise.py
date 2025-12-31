# 問題22
# 設計メモ
# ※2つ目の文字列をforループまわし、1つ目の文字列に含まれるかを判定
# ```
# input()関数で「1つ目の文字列を入力してください > 」、受け取った文字列を変数words_1に格納
# input()関数で「2つ目の文字列を入力してください > 」、受け取った文字列を変数words_2に格納 
# 空の文字列duplicate_charsを宣言
# for文でwords_2をまわして1文字ずつ取り出し、変数wに格納
# もしwがwords_1に含まれる、かつ、duplicate_charsに含まれない場合は、duplicate_charsを「duplicate_chars+w」で更新
# ループ終了後、「重複する文字列 : 」とduplicate_charsをprintで出力

words_1 = input("1つ目の文字列を入力してください > ")
words_2 = input("2つ目の文字列を入力してください > ")
duplicate_chars = ""
for w in words_2:
    if w in words_1 and w not in duplicate_chars:    # andの後ろを「not in duplicate_chars:」だけで「w」を忘れてSyntaxError
        duplicate_chars += w
print(f'重複する文字列 : {duplicate_chars}')
