# 問題4
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 32},
    {"name": "Diana", "age": 15},
    {"name": "Eve", "age": 20}
]
# 20歳以上30歳未満 のユーザーの名前だけを新しいリストとして作成せよ
# 最後にそのリストを出力せよ

# 設計メモ
# 0.空のリストusers_nameを作成
# 1.for文で、リストusersの要素(辞書)を1つずつ取り出して変数userに格納していく
# 2.変数userに格納された辞書のKey”age”に該当するValueが、20以上30未満であるかを調べる
# 3.もし条件を満たした場合は、その辞書のKey”name”に該当するValueをリストusers_nameに要素として追加する
# 4.for文の外でusers_nameを出力する

users_name = []
for user in users:
    if 20 <= user["age"] <30:
        users_name.append(user["name"])
print(users_name)    # ['Alice', 'Eve']

print("-" * 20)# ----------
# 問題5
orders = [
    {"id": 1, "price": 1200},
    {"id": 2, "price": 500},
    {"id": 3, "price": 3000},
    {"id": 4, "price": 800},
    {"id": 5, "price": 1500}
]
# 1000円以上の注文の個数 を数えて出力せよ
# 処理は 関数として定義すること
# 関数は引数として orders を受け取る・条件に合う注文の 個数を return する

# 【解答1】　「数だけ欲しい」とき・処理が速い
# 設計メモ
# 0.関数order_countsを定義する(引数はリストorders_list、戻り値は条件に合う注文の個数）
# 1.カウンタ変数icountを0で初期化して宣言
# 2.for文で、リストorders_listの要素(辞書)を1つずつ取り出して変数order_dictに格納していく
# 3.if文で、order_dictに格納された辞書のKey"price"に該当するValueが1000以上であるかを判定
# 4.条件に合えば、カウンタ変数icountに1を足す
# 5.for文の外でカウンタ変数icountを戻り値として設定する
# 6.関数order_countsの戻り値を出力する

def order_counts(orders_list):
    icount = 0
    for order_dict in orders_list:
        if order_dict["price"] >= 1000:
            icount += 1
    return icount

print(order_counts(orders))    # 3

# 【解答2】　「中身を後で使用したい」とき・Flaskでよく使用
# 設計メモ
# 0.関数order_countsを定義する(引数はリストorders_list、戻り値は条件に合う注文の個数）
# 1.空のリストfiltered_ordersを作成
# 2.for文で、リストorders_listの要素(辞書)を1つずつ取り出して変数order_dictに格納していく
# 3.if文で、order_dictに格納された辞書のKey"price"に該当するValueが1000以上であるかを判定
# 4.条件に合えば、リストorder_dictにorder_dictを要素として追加する
# 5.for文の外で、order_dictの要素の数を戻り値として設定する
# 6.関数order_countsの戻り値を出力する

def order_counts(orders_list):
    filtered_orders = []
    for order_dict in orders_list:
        if order_dict["price"] >= 1000:
            filtered_orders.append(order_dict)
    return len(filtered_orders)    # 間違ってlen()の引数をorder_dictと書いて出力が「2」になったので修正

print(order_counts(orders))    # 3
    