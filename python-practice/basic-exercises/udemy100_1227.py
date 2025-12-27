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
# 入力した英単語を大文字に変換するプログラムを作成してください。

# 英単語を入力してください > Python
# 変換後の文字列 : PYTHON

# 設計メモ
# ※Pythonでは大文字と小文字は区別されて別の文字として扱われるから、inputで受け取る不特定の文字列をメソッドや関数なしで操作するのは難しそう。
# 　なぜ？　→　inputで受け取る不特定の文字列を、自力で判定・変換するのは大変だから。
# 　　　　　→　1文字ずつfor文で回してaならA、bならB…と、アルファベット26文字分の対応が必要
# ※なので小文字を大文字に変換する方法を検索したら、すべての文字を大文字に変換する.upper()がヒットした。

# input（）で　英単語を入力してください > 　、受け取った英単語を変数english_wordに格納
# english_wordを.upper()ですべて大文字に変換するしたものを、english_wordに格納
# 「変換後の文字列 : 」とenglish_wordをprintで出力

english_word = input(f"英単語を入力してください > ").upper()
print(f'変換後の文字列 : {english_word}')

print("-" * 20)# ----------
# 問題21
# 入力した英単語の先頭1文字が、小文字だったら大文字に変換、大文字だったら2回反復するプログラムを作成してください。
# 大文字の例：
# ```
# 英単語を入力してください > Python
# 変換後の文字列 : PythonPython
# ```
# 小文字の例：
# ```
# 英単語を入力してください > python
# 変換後の文字列 : Python
# ```

# 設計メモ
# ※調べたところ、入力された英単語の先頭1文字だけが大文字か小文字かを判定する関数やメソッドはなさそう。
# ※タイトルケースかの判定、全ての文字が大文字かを判定、なら存在した。
# ※全ての文字が大文字かを判定する「.isupper()」を、インデックスを指定して使うことはできないか実験
# ※無事にインデックスを指定して1文字だけ判定できたので、これを使用して書いてみる。
# ```
# inputで「英単語を入力してください > 」、受け取った文字列を変数e_Wordに格納
# もしe_Wordの先頭1文字が大文字なら、「e_Wordを2回反復した文字列」をe_Wordに格納
# それ以外の場合は、「e_Wordの先頭1文字を大文字に変換した文字列」をe_Wordに格納(実は間違い)
# if文の外で、「変換後の文字列 : 」とe_Wordをprintで出力
# ※if文で操作した文字列をe_Wordに入れ直しておくことで、printで出力するのはラスト1行のみで済む

e_Word = input("英単語を入力してください > ")
if e_Word[0].isupper():
    e_Word *= 2     # スマートな演算子をググった　当初、数値じゃないのに「e_Word **= 2 」と書いてTypeErrorに。
else:
    e_Word = e_Word[0].upper() +  e_Word[1:]   # 当初、「e_Word = e_Word[0].upper()」と書いて「P」だけ出力された。
print(f'変換後の文字列 : {e_Word}')

print("-" * 20)# ----------
# 問題22
# 2つの文字列を入力して、重複する部分だけ出力するプログラムを作成してください。
# ```
# 1つ目の文字列を入力してください > Python
# 2つ目の文字列を入力してください > PHP
# 重複する文字列 : P
# ```

# 設計メモ
# ※2つの文字列で重複する文字を抜き出す関数やメソッドがないか、1つ目の文字列と2つ目の文字列を同時にforループさせる方法はないかググったが、
# 　どれも今ある知識の範疇を超えていた。検索結果を眺めているうち、ふと、普通にシンプルな方法を思いついた。↓
# ※どちらかの文字列をforループで1つずつ取り出して、取り出した文字が2つ目の文字列に含まれているかを判定し、含まれているなら新たな文字列に追加する
# ```
# 空の文字列common_charsを宣言
# inputで「1つ目の文字列を入力してください > 」、受け取った文字列を変数str_1に格納
# inputで「2つ目の文字列を入力してください > 」、受け取った文字列を変数str_2に格納
# for文でstr_1の文字を1つずつ取り出して、変数iに格納
# もしiがstr_2に含まれる場合は、common_charsにiを追加していく。
# if文の外で、「重複する文字列 : 」とcommon_charsをprintで出力

# 解答1：重複する文字があれば、全部拾うバージョン　→　str_1 = "banana"・str_2 = "an"なら出力が「anana」になる
common_chars = ""
str_1 = input("1つ目の文字列を入力してください > ")
str_2 = input("2つ目の文字列を入力してください > ")
for i in str_1:
    if i in str_2:
        common_chars += i
print(f'重複する文字列 : {common_chars}')

# 解答2：重複する文字を各1つだけ拾うバージョン　→　str_1 = "banana"・str_2 = "an"なら出力が「an」になる
common_chars = ""
str_1 = input("1つ目の文字列を入力してください > ")
str_2 = input("2つ目の文字列を入力してください > ")
for i in str_1:
    if i in str_2 and i not in common_chars:    # iがstr_2に含まれる、かつ、common_charsには含まれない場合、
        common_chars += i
    elif i in str_2 and i in common_chars:    # iがstr_2に含まれる、かつ、common_charsにも含まれる場合、→　「elif～continue」いらない！
        continue
print(f'重複する文字列 : {common_chars}')