# 問題29
# 組み込み関数を使って、リスト` [1, 5, 3, 2, 4]`に格納されている数値の最大値を出力するプログラムを作成してください。
# ```
# リスト内の最大値 : 5
# ```

# 設計メモ
# ※検索したところ、リストの要素の最大値を求めるにはmax()関数が使える
# ```
# [1, 5, 3, 2, 4]を要素とするリストlを宣言
# max()関数に引数としてlを渡し、戻り値を変数l_maxに格納
# 「リスト内の最大値 : 」とl_maxをprintで出力

l = [1, 5, 3, 2, 4]
l_max = max(l)
print(f'リスト内の最大値 : {l_max}')

print("-" * 20)# ----------
# 問題30
# リスト`[1, 2, 2, 3, 3, 4, 5]`から重複している値を削除するプログラムを作成してください。
# ```
# 重複削除したリスト : [1, 2, 3, 4, 5]
# ```

# 設計メモ
# ※リストから重複している要素を削除する方法を検索したところ、dict.fromkeys()メソッドでいったん元リストを辞書に変換し、重複が消えた後に再度リストに戻す方法が使える
# ※辞書化したときに重複したKeyは無視される（辞書の仕様）、かつ、set型にキャストする方法と違って元リストの要素の並び順を壊すこともない
# ```
# [1, 2, 2, 3, 3, 4, 5]を要素とするリストlを宣言
# dict.fromkeys()メソッドに引数としてlを渡して辞書化したものを変数l_dictに格納
# 「重複削除したリスト : 」とl_dictをリスト型にキャストしたものをprintで出力

l = [1, 2, 2, 3, 3, 4, 5]
l_dict = dict.fromkeys(l)
print(f'重複削除したリスト : {list(l_dict)}')

# 模範解答　set型にキャスト。要素の並び順は気にしないでOKなやつだった
l = [1, 2, 2, 3, 3, 4, 5]
new_l = list(set(l))
print(f'重複削除したリスト : {new_l}')

print("-" * 20)# ----------
# 問題31
# リスト`['Python', 'Ruby', 'PHP', 'JavaScript']`に格納されている文字列の中で、一番短い単語を出力するプログラムを作成しましょう。
# ```
# 一番短い単語 : PHP
# ```

# 設計メモ
# ※調べたところ、min()関数とlen()関数を使えばよさそう
# ※min()関数の引数に、リストのインデックスが指定可能
# ```
# ['Python', 'Ruby', 'PHP', 'JavaScript']を要素とするリストwords_listを宣言
# min()関数の引数として、「words_listのインデックス0に該当する文字列の長さ」、「words_listのインデックス1に該当する文字列の長さ」、
# 　同じようにインデックス3まで渡して、かえってきた戻り値を変数shortest_wordに格納
# 「一番短い単語 : 」とshortest_wordをprintで出力

words_list = ['Python', 'Ruby', 'PHP', 'JavaScript']
shortest_word = min(len(words_list[0]), len(words_list[1]), len(words_list[2]), len(words_list[3])) 
print(f'一番短い単語 : {words_list[shortest_word]}')    # 一番短い単語 : JavaScript　✖失敗

# 再チャレンジ
# 設計メモ
# ※min()関数の戻り値は最小値そのものだから、最後にwords_listの文字列を出力させようとしても無理だった
# ※なのでとりあえず関数なしで解いてみる
# ```
# ['Python', 'Ruby', 'PHP', 'JavaScript']を要素とするリストwords_listを宣言
# 1番短い単語をとりあえず先頭の要素であると仮定するため、変数shortest_wordにwords_listのインデックス0に該当する要素を格納
# for文で、words_listから「インデックス0以外の要素」を1つずつ取り出して変数wに格納する
# もしwの文字列の長さが、shortest_wordの文字列の長さよりも短い場合は、shortest_wordをwで更新する
# ループ終了後、「一番短い単語 : 」とshortest_wordをprintで出力

words_list = ['Python', 'Ruby', 'PHP', 'JavaScript']
shortest_word = words_list[0]
for w in words_list[1:]:
    if len(w) < len(shortest_word):
        shortest_word = w
print(f'一番短い単語 : {shortest_word}')

print("-" * 20)# ----------
# 復習！
# 今日の復習は、文字型：問題16～25まで。問題文は割愛
print("-" * 20)# ----------
# 問題16　◎
# 設計メモ
# ※len()を使わずに文字列の長さを出力　→　forループで文字列を回して1周終わったときのカウンタ変数を出力
# ```
# input()関数で「文字を入力してください > 」、受け取った文字列を変数wordに格納
# カウンタ変数countを0で初期化して宣言
# for文で、wordの文字列を1文字ずつ取り出して_（以降は使わない変数のため）に格納
# countを、「count+1」に更新
# ループ終了後、「Pythonの文字数 : 」とcountをprintで出力

word = input("文字を入力してください > ")
count = 0
for _ in word:
    count += 1
print(f'{word}の文字数 : {count}')

print("-" * 20)# ----------
# 問題17　◎
# 設計メモ
# ※最初の文字はインデックス0、最後の文字はインデックス-1
# ```
# input()関数で「文字を入力してください > 」、受け取った文字列を変数sに格納
# 「sの最初の文字 : 」とsのインデックス0の文字をprintで出力
# 「sの最後の文字 : 」とsのインデックス-1の文字をprintで出力

s = input("文字を入力してください > ")
print(f'{s}の最初の文字 : {s[0]}')
print(f'{s}の最後の文字 : {s[-1]}')

print("-" * 20)# ----------
# 問題18　△
# 設計メモ
# ※文字列の出現頻度　出力結果が辞書　→　文字列をループさせて1つずつ「空の辞書に存在するKeyであるか」を判定し、
# ※真ならすでに存在するKeyのValueを+1して更新
# ※その他の場合は新たにKeyとValue（1）を要素として追加する感じで実装
# ```
# input()関数で「文字を入力してください > 」、受け取った文字列を変数wordに格納
# 空の辞書word_dictを宣言
# for文で、wordの文字列を1つずつ取り出し、変数wに格納
# もし、wがword_dictの中にKeyとして存在するなら、word_dictのKey「w」に該当するValueに+1をして更新
# その他の場合は、新たに「w」をKeyとして、「1」をValueとしてword_dictの要素を追加
# word_dictをprintで出力

word = input("文字を入力してください > ")
word_dict = {}
for w in word:
    if w in word_dict:
        word_dict[w] += 1
    else:
        word_dict[w] = 1
print(word_dict)

print("-" * 20)# ----------
# 問題19　△　別解×
# 設計メモ
# ※英単語から母音a, i, u, e, oを取り除くには、ループで英単語をまわして、あらかじめリスト化しておいた母音リストの中に含まれているか否かを判定
# ```
# input()関数で「文字列を入力してください > 」、受け取った文字列を変数wordsに格納
# a, i, u, e, oを要素とするリストvowel_listを宣言
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
new_word = ""    # 空の文字列　文字列は足し算、掛け算可能だからわざわざリストにしなくてよい！忘れてた！
for w in words:
    if w in vowel_list:
        continue
    new_word += w
print(f'作成した文字列 : {new_word}')

print("-" * 20)# ----------
# 別解　※replace()を使う
# input()関数で「文字列を入力してください > 」、受け取った文字列を変数wordsに格納
# a, i, u, e, oを要素とするリスト vowel_list を宣言
# for文でvowel_listの文字を1つずつ取り出し、変数vに格納
# wordsの中に含まれるvを、replace()で空白に置換し、new_wordに格納
# ループ終了後、「作成した文字列 : 」とnew_wordをprintで出力

words = input("文字列を入力してください > ")
vowel_list = ["a", "i", "u", "e", "o"]
for v in vowel_list:
    new_word = words.replace(v, "")
print(f'作成した文字列 : {new_word}')

print("-" * 20)# ----------
# 問題20 ◎
# 設計メモ
# ※すべての文字列を大文字に変換するには、upper()メソッドが使える
# ```
# input()関数で「英単語を入力してください > 」、受け取った文字列を変数wordsに格納
# 「変換後の文字列 : 」と、upper()メソッドで大文字化したwordsをprintで出力

words = input("英単語を入力してください > ")
print(f'変換後の文字列 : {words.upper()}')

print("-" * 20)# ----------
# 問題21　✖
# 設計メモ
# ※文字列(1文字でも)を大文字に変換するには、upper()メソッドが使える
# ※文字が小文字であるかの判定は、islower()メソッドが使える
# ```
# input()関数で「文字列を入力してください > 」、受け取った文字列を変数 words に格納
# もし、wordsのインデックス0に該当する文字が小文字の場合、upper()メソッドで大文字化してwordsに格納しなおす
# その他の場合は、wordsを「wordsの二乗」で更新
# 「変換後の文字列 : 」と、wordsをprintで出力

words = input("文字列を入力してください > ")
if words[0].islower():
    words = words[0].upper() + words[1:]    # 「+ words[1:]」を書かずに出力が「P」だけに
else:
    words = words * 2    # 「words ** 2」と書いてTypeErrorに。文字列の乗算はNG。掛け算なら可能
print(f'変換後の文字列 : {words}')

print("-" * 20)# ----------
# 問題22　✖
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

print("-" * 20)# ----------
# 問題23

print("-" * 20)# ----------
# 問題24

print("-" * 20)# ----------
# 問題25

