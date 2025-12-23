# 問題6
# 数字の1から30のうち、3の倍数だけ出力するプログラムを作成しましょう。
# 3
# 6
# 9
# 12
# 15
# 18
# 21
# 24
# 27
# 30

# 解答A ✖問題文の「1から30のうち、」を満たしてない！
# 設計メモ
# ・for文でrange（）で3から30までの数を2つ飛ばしで取り出し、変数multiple_of_3に格納していく
# ・変数multiple_of_3をprintで出力
for multiple_of_3 in range(3, 31, 3):    # 3つ目の引数を何度も間違えた　「3,4,5,6」「6,7,8,9」「9,10,11,12」と数えると良い
    print(multiple_of_3)

print("-" * 20)# ----------
# 解答B 〇こっちが正解
# 設計メモ
# ・for文でrange（）で1から30までの数を1つずつ取り出し、変数numに格納していく
# ・変数numを3で割ったときの余りが0なら、
# ・変数numをprintで出力
for num in range(1, 31):
    if num % 3 == 0:
        print(num)

print("-" * 20)# ----------
# 問題7
# 数字の1から30のうち、
# - 3の倍数のとき”fizz”
# - 5の倍数のとき”buzz”
# - 15の倍数のとき”fizzbuzz”
# - その他の場合はその数字
# を出力するプログラムを作成しましょう。

# 1
# 2
# fizz
# 4
# buzz
# (中略)
# 28
# 29
# fizzbuzz

# 設計メモ
# for文、range（）で1から30の数を1つずつ取り出して変数iに格納していく
# iが15の倍数なら、”fizzbuzz”と出力
# iが3の倍数なら、”fizz”と出力
# iが5の倍数なら、”buzz”と出力
# その他の場合はiを出力

for i in range(1, 31):
    if i % 15 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)






