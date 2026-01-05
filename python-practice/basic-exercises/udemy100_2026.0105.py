# 問題42　※昨日の復習
# リスト内に重複している値が入っているか確認するプログラムを作成してください。
# `l = [1, 2, 3, 3]`の場合 : 
# ```
# 重複している値があります。
# ```
# `l = [1, 2, 3]`の場合 : 
# ```
# 重複する値がありません。
# ```

# forループバージョン
# 設計メモ
# 「見たことがある」の要素を記録しておくための空のリストを変数seenに格納
# 重複があるかを判定するためのフラグ変数duplicate_existsを初期値falseで宣言
# for文でlの要素を1つずつ取り出し、変数iに格納
# もしiが「見たことあるリスト」であるseenに含まれる場合は、duplicate_existsにtrueを格納し、forループを強制終了
# （省略：それ以外の場合、）たった今「見たことがある」状態になったiを、seenに要素として追加
# ループ終了後、もしduplicate_exists（省略：に格納されているのがtrue）ならば、
# 「重複している値があります。」をprintで出力
# それ以外の場合は「重複する値がありません。」をprintで出力

l = [1, 2, 3, 3]
seen = []
duplicate_exists = False
for i in l:
    if i in seen:
        duplicate_exists = True
        break
    seen.append(i)
if duplicate_exists:
    print("重複している値があります。")
else:
    print("重複する値がありません。")

# set()で集合にした場合の要素の数で重複を判定するバージョン
l = [1, 2, 3, 3]
if len(l) > len(set(l)):
    print("重複している値があります。")
else:
    print("重複する値がありません。")
