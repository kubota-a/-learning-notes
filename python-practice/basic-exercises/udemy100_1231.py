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
# 今日の復習は、文字型：問題16～25まで。


print("-" * 20)# ----------
# 問題32

print("-" * 20)# ----------
# 問題33

print("-" * 20)# ----------
# 問題34