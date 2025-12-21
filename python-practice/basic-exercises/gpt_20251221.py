# 問題3
products = [
    {"name": "apple", "price": 120},
    {"name": "banana", "price": 80},
    {"name": "cherry", "price": 300},
    {"name": "orange", "price": 150}
]

# 要求100円以上200円未満の商品名だけを新しいリストとして作成せよ
# 最後にそのリストを出力せよ

# 設計メモ
# 1.リストproductsの4つの要素の、それぞれのキー"price"のValueを1つずつ取り出して、
# 「100円以上200円未満」であるかどうかを調べる
# 2.そのValueが条件に合う場合は、新しいリストに要素としてその「商品名だけ」を追加していく。
# 3.最後に完成した新しいリストを出力する

product_name = []     # 新しいリストを空で作成
for product in products:    # リストproductsから要素(辞書)を1つずつ取り出して変数productに入れていく
    if 100 <= product["price"] <200:    # もし辞書productのキー”price”に該当するValueが100以上200未満であるなら、
        product_name.append(product["name"])    # リストProduct_nameに辞書productのキー"name"に該当するValueを要素として追加する。
print(product_name)    # リストProduct_nameを出力する　['apple', 'orange']

