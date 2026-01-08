# 問題45
# 以下のリストで、全ての要素前に文字列”list”を追加するプログラムを作成してください。
# ※使用するリスト : 
# ```
# l = [1, 2, 3, 4, 5]
# ```
# 期待する出力
# ```
# "list"を追加したリスト : ['list', 1, 'list', 2, 'list', 3, 'list', 4, 'list', 5]
# ```

# 設計メモ
# ※問題文は「以下のリストで、全ての要素前に文字列”list”を追加する」なので、新しいリストを作成するのではなく既存のリストlに直接変更を与える必要がある。
# ※調べたところ、インデックスを指定して要素を追加するにはinsert() メソッドを使用。ただし、複数のインデックスを指定できないため、工夫してforループさせることにする。
# ※insert() メソッドで要素を追加した場合、指定したインデックスの位置に元々あった要素とその後の要素は、1つずつ右にシフトされる。
# ※'list'を追加したい位置のインデックス番号は、「0、2、4、6、8」と偶数。
# ```
# l = [1, 2, 3, 4, 5]を宣言
# カウンタ変数countを0で初期化して宣言
# for文でlを回す（後で使用しないので変数は_でOK）
# insert() メソッドで、lのインデックス番号「count」の位置に、"list"を要素として追加
# countに「count+2」を格納しなおす
# 「"list"を追加したリスト : 」とlをprintで出力

# 失敗コード　lを回している最中にlの要素を増やしていく処理をしてるから無限ループしてしまった
l = [1, 2, 3, 4, 5]
count = 0
for _ in l:
    l.insert(count, 'list')    # forで回しているリストに、ループ中に「要素が増減する」変更を加えたらダメ！！前も同じ間違いした！
    count += 2
print(f'"list"を追加したリスト : {l}')

# 再チャレンジ1 　for文で回すのをlのコピーにするバージョン
l = [1, 2, 3, 4, 5]
l_copy =l[:]    # lの要素をまるごとコピーしたリストl_copyを宣言
count = 0
for _ in l_copy:    # lは回してないから要素の数が変わってもOK
    l.insert(count, 'list') 
    count += 2
print(f'"list"を追加したリスト : {l}')

# 再チャレンジ2　for文で回すのをlの要素の数を渡したrange()にするバージョン
l = [1, 2, 3, 4, 5]
count = 0
for _ in range(len(l)):    # len()に渡したのはループ前のlの要素数だから回数が固定されてる！
    l.insert(count, 'list') 
    count += 2
print(f'"list"を追加したリスト : {l}')

# 模範解答　カウンタ変数使わない
l = [1, 2, 3, 4, 5]
for i in range(0, 10, 2):     # なぜインデックス10まで？　→　最終的な['list', 1, 'list', 2, 'list', 3, 'list', 4, 'list', 5]の長さ
    l.insert(i, 'list') 
print(f'"list"を追加したリスト : {l}')

print("-" * 20)# ----------
# 問題46
# 以下のリストで文字列”Python”が含まれている要素を削除するプログラムを作成してください。
# ※使用するリスト : 
# ```
# l = ['Python1', 'Java1', 1, 'Python2', 'Java2', 2]
# ```
# ▼期待する出力
# ```
# 文字列"Python"を削除したリスト : ['Java1', 1, 'Java2', 2]
# ```

# 設計メモ
# ※実験したところ、リストlのある要素に「Python」が含まれているかは、「if 'Python' in l[0]:」で判定できる
# ※lの要素を削除していくから、for文で回すのはl以外！　→　さっきみたいに、range()にループ前のlの長さを渡して回すことにする
# ```
# l = ['Python1', 'Java1', 1, 'Python2', 'Java2', 2]を宣言
# for文で、ループ前のlの長さを渡したrange()を回し、インデックス番号を変数iに格納
# もし、iのデータ型がstr型の場合は、下記を実行
# もし、lのインデックス番号iにあたる要素に「Python」が含まれている場合は、lから、lのインデックス番号iにあたる要素を削除する
# 「文字列"Python"を削除したリスト : 」とlをprintで出力

# 失敗　実行したら l = ['Python1', 'Java1', 1, 'Python2', 'Java2', 2]がそのままかえってきた。
l = ['Python1', 'Java1', 1, 'Python2', 'Java2', 2]
for i in range(len(l)):
    if isinstance(i, str):
        if 'Python' in l[i]:
            del l[i]
print(f'文字列"Python"を削除したリスト : {l}')

# 再チャレンジ　失敗
l = ['Python1', 'Java1', 1, 'Python2', 'Java2', 2]
for i in range(len(l)):
    if isinstance(l[i], str):    # isinstance関数に、直接lのインデックス指定はできない！
        if 'Python' in l[i]:
            del l[i]
print(f'文字列"Python"を削除したリスト : {l}')

# 再々チャレンジ　delやってる以上、IndexErrorは解決せず
l = ['Python1', 'Java1', 1, 'Python2', 'Java2', 2]
for i in range(len(l)):
    element = l[i]    # いったん変数にlのインデックスiにあたる要素を格納する
    if isinstance(element, str):
        if 'Python' in element:
            del l[i]
print(f'文字列"Python"を削除したリスト : {l}')

# 新しいリストを作って良いなら簡単！
l = ['Python1', 'Java1', 1, 'Python2', 'Java2', 2]
new_l = []
for i in l:
    if isinstance(i, str):
        if 'Python' not in i:
            new_l.append(i)
    else:    # 当初else文書くの忘れて文字列型以外の要素が追加されず、['Java1', 'Java2']だけになってしまった
        new_l.append(i)
print(f'文字列"Python"を削除したリスト : {new_l}')

# 新しいリスト版　もっとスマートなコード
l = ['Python1', 'Java1', 1, 'Python2', 'Java2', 2]
new_l = []
for i in l:
    if isinstance(i, str) and 'Python' in i:    # もしiが文字列型で、かつ、iに「Python」が含まれている場合は、
        continue    # このループの残りの処理をスキップして次のiへ進む
    new_l.append(i)    # iが上記の条件に当てはまらなければ、iをnew_lに要素として追加
print(f'文字列"Python"を削除したリスト : {new_l}')

# 模範解答は実務ではNGな内容だったため無視☆