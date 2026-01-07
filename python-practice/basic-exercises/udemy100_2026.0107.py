# 問題43
# 以下のリストを、それぞれのデータ型でソートするプログラムを作成してください。
# ※使用するリスト : 
# ```
# l = [4, 'aaa', 2, 'ddd', 'ccc', 3, 1, 'bbb']
# ```
# ▼期待する出力
# ```
# ソートしたリスト : [1, 2, 3, 4, 'aaa', 'bbb', 'ccc', 'ddd']
# ```

# 設計メモ
# ※並べ替えはsorted関数で行うが、異なるデータ型が混在すると並べ替えできないので
# ※いったんデータ型ごとにリストを分けて、ソート後に結合させる方針でいく
# l = [4, 'aaa', 2, 'ddd', 'ccc', 3, 1, 'bbb']を宣言
# 新しいリストl_intを、リスト内包表記でint型のみ抜き出して作成
# 新しいリストl_strを、リスト内包表記でstr型のみ抜き出して作成
# l_intをソートしたリストと、l_strをソートしたリストを結合し、変数new_lに格納
# 「ソートしたリスト : 」とnew_lをprintで出力

l = [4, 'aaa', 2, 'ddd', 'ccc', 3, 1, 'bbb']
# lをforループで回し、iに格納・条件：int型のものを抜き出す
l_int = [i for i in l if isinstance(i, int)]
l_str = [i for i in l if isinstance(i, str)]
new_l = sorted(l_int) + sorted(l_str)
print(f'ソートしたリスト : {new_l}')

print("-" * 20)# ----------
# 問題44
# 指定したリストに文字列が入っているか判定するプログラムを作成してください。
# `l = [1, 2, 3, '4', 5]`の場合 : 
# ```
# 文字列が入っています。
# ```
# `l = [1, 2, 3, 4, 5]`の場合 : 
# ```
# 文字列は入っていません。
# ```

# 設計メモ
# ※isinstanceではリスト内の要素を一度には判定できない
# ※→for文で1つずつ判定していって、1つでも判定がtrueになったらループ終了する仕様にする
# 任意のリストを宣言
# フラグ変数t_fをfalseで初期化して宣言
# for文で任意のリストの要素を1つずつ取り出し、変数iに格納
# iがstr型なら、t_fにtrueを格納し、ループを終了する
# ループ終了後、もしt_fに格納されているのがtrueなら、
# 　「文字列が入っています。」をprintで出力

l = [1, 2, 3, '4', 5]
t_f = False
for i in l:
    if isinstance(i, str):
        t_f = True
        break
if t_f:
    print(f'文字列が入っています。')
else:
    print(f'文字列は入っていません。')

print("-" * 20)# ----------
# 模範解答　any()を使う
l = [1, 2, 3, '4', 5]
if any(isinstance(i, str) for i in l):    # anyの()内に1つでもtrueが入ってい要れば、anyはtrueを返す！
    print(f'文字列が入っています。')
else:
    print(f'文字列は入っていません。')    

print("-" * 20)# ----------
# anyの()内に1つでもtrueが入ってい要れば、anyはtrueを返す！
print(any([True, False]))    # True
print(any([False, False]))    # False