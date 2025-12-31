

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