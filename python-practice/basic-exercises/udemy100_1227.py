# 問題17
# 入力した文字列の、最初と最後の文字を出力するプログラムを作成してください。

# 文字を入力してください > Python
# Pythonの最初の文字 : P
# Pythonの最後の文字 : n

# 設計メモ最初と最後の文字のインデックスを指定する
# input（）で　文字を入力してください > 　、受け取った文字を変数wordに格納
# wordの最初の文字 : 　、wordのインデックス0の文字　をprintで出力
# wordの最後の文字 : 　、wordのインデックス-1の文字　をprintで出力

word = input("文字を入力してください > ")
print(f'{word}の最初の文字 : {word[0]}')
print(f'{word}の最後の文字 : {word[-1]}')

print("-" * 20)# ----------
# 問題18
# 入力した文字列に登場する文字の、出現頻度をカウントするプログラムを作成してください。

# 文字列を入力してください > PythonPractice
# {'P': 2, 'y': 1, 't': 2, 'h': 1, 'o': 1, 'n': 1, 'r': 1, 'a': 1, 'c': 2, 'i': 1, 'e': 1}

# 設計メモ
# ※出力結果が辞書　→　おおまかには「for文で取り出した文字をKeyとして・各文字の出現をValueとして空の辞書に追加していく」ようなプログラムを書く
# ※初めての文字が取り出されたら、「その文字がKey、「1」がValue」の要素として辞書に追加する
# ※同じ文字が取り出されたら、その文字がKeyとなっている既存の要素のValueの値を1つ増やして更新する

# input（）で　文字を入力してください > 　、受け取った文字を変数wに格納
# 空の辞書w_dictを宣言
# for文でwの文字を1つずつ取り出して、変数iに格納
# もしiが辞書w_dictの中に存在していなければ、「iがKey、「1」がValue」の要素として辞書辞書w_dictに追加する
# それ以外の場合、「iがKeyとなっている既存の要素のValueの値」を1つ増やして更新する
# for文を出てから、辞書w_dictをprintで出力

w = input("文字を入力してください > ")
w_dict = {}
for i in w:
    if i not in  w_dict:
        w_dict[i] = 1
    else:
        w_dict[i] += 1
print(w_dict)

# もっとスマートなコード　get関数を使うと、条件分岐を書く必要がなくなって4行が1行にできる！
w = input("文字を入力してください > ")
w_dict = {}
for i in w:
    w_dict[i] = w_dict.get(i, 0) + 1
    # 「i」というKeyが存在するなら既存のValueに+1、「i」というKeyが存在しないならValueデフォルト値0に+1して新しい要素を追加
print(w_dict)

# △別解1
w = input("文字を入力してください > ")
w_dict = {}
for i in w:
    if i not in  w_dict.keys():    # .keysを使っているが、「辞書に対して in を使ったら キーを調べる」言語仕様なので必要なし。
        w_dict[i] = 1
    else:
        w_dict[i] += 1
print(w_dict)

print("-" * 20)# ----------
# 問題19
# 入力した英単語から、母音(a, i, u, e, o)を取り除くプログラムを作成してください。

# 文字列を入力してください > Python
# 作成した文字列 : Pythn

# 設計メモ
# ※文字列の引き算はできない　→　for文で文字を1つずつ取り出し、母音(a, i, u, e, o)以外なら新たな文字列に追加していくことにする

# input（）で　文字列を入力してください > 　、受け取った文字を変数wordに格納
# 空白の文字列を格納した変数new_wordを宣言
# for文でwordの文字を1つずつ取り出して、変数wに格納
# もしwがaまたはiまたはuまたはeまたはoではないなら、new_wordに追加する
# for文の外で、作成した文字列 : 　と、new_wordをprintで出力

# 失敗したコード
word = input("文字列を入力してください > ")
new_word = ""
for w in word:
    if w != "a" or w != "i" or w != "u" or w != "e" or w != "o":    # orは1つでもtrueなら「true」を返すから、母音までnew_wordに追加された
        # 「and」なら出力結果は正解になるけど読みにくい
        new_word = new_word + w    # 当初、頭に「new_word =」を付け忘れて何も出力されなかった
print(f'作成した文字列 : {new_word}')

# 再チャレンジ
# 設計メモ
# ※1文字ずつ「母音a, i, u, e, oが要素となっているリスト」に含まれるかを判定し、含まれないなら新しい文字列に追加する

# input（）で　文字列を入力してください > 　、受け取った文字を変数wordに格納
# 母音a, i, u, e, oが要素となっているリストvowel_listを宣言
# 空白の文字列を格納した変数new_wordを宣言
# for文でwordの文字を1つずつ取り出して、変数wに格納
# もしwがvowel_listに含まれてないなら、new_wordに追加する
# for文の外で、作成した文字列 : 　と、new_wordをprintで出力

word = input("文字列を入力してください > ")
vowel_list = ["a", "i", "u", "e", "o"]
new_word = ""
for w in word:
    if w not in vowel_list:
        new_word = new_word + w    # 当初、頭に「new_word =」を付け忘れて何も出力されなかった
        # 「new_word =」がなければ単に計算しただけなのでnew_wordの文字列は変わらないから、必ず変数に代入し直す必要がある
print(f'作成した文字列 : {new_word}')

# 模範解答　「除外したい条件」があるときに使いやすい
word = input("文字列を入力してください > ")
vowel_list = ["a", "i", "u", "e", "o"]
new_word = ""
for w in word:
    if w in vowel_list:    # もしwがvowel_listに含まれるなら、（除外条件を先に書くスタイル）
        continue    # このループの残りを飛ばして次へ！　=　「もし母音リストに該当するなら、何もせず次の文字へ行け！」
    new_word += w
print(f'作成した文字列 : {new_word}')

# 別解　新たな文字列を作らずに、もとの文字列からダイレクトに母音を削除する方法
word = input("文字列を入力してください > ")
vowel_list = ["a", "i", "u", "e", "o"]
for w in vowel_list:    # 母音の入ったリストvowel_listをループの対象とする
    word = word.replace(w, "")    # 変数Wordを、「wを空白に置換した文字列」に更新する
print(f'作成した文字列 : {word}')    # Wordをprintで出力

print("-" * 20)# ----------
# 問題20

print("-" * 20)# ----------
# 問題21

print("-" * 20)# ----------
# 問題22