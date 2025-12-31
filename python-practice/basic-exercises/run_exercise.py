# 問題19　△
# 設計メモ
# ※英単語から母音a, i, u, e, oを取り除くには、ループで英単語をまわして、あらかじめリスト化しておいた母音リストの中に含まれているか否かを判定
# ```
# input()関数で「文字列を入力してください > 」、受け取った文字列を変数wordsに格納
# a, i, u, e, oを要素とするリスト vowel_list を宣言
# 空のリストnew_wordを宣言
# for文でwordsの文字を1つずつ取り出し、変数wに格納
# もし、wがvowel_listに含まれないなら、new_wordにwを要素として追加
# ループ終了後、join()メソッドでnew_wordを文字列に変換し、それを変数new_word_strに格納
# 「作成した文字列 : 」とnew_word_strをprintで出力

words = input("文字列を入力してください > ")
vowel_list = ["a", "i", "u", "e", "o"]
new_word = []
for w in words:
    if w not in vowel_list:
        new_word.append(w)
new_word_str = "".join(new_word)
print(f'作成した文字列 : {new_word_str}')

print("-" * 20)# ----------
# 模範解答
words = input("文字列を入力してください > ")
vowel_list = ["a", "i", "u", "e", "o"]
new_word = ""
for w in words:
    if w in vowel_list:
        continue
    new_word += w
print(f'作成した文字列 : {new_word}')
