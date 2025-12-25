# 問題10
# 数字の1から40のうち、3の倍数かつ"3"が付く数字だけを格納した「リスト」を作成して、下記のように表示しましょう。
# 作成したリスト : [3, 30, 33, 36, 39]

# 設計メモ
# 空のリストthreeを宣言
# for文でrange（）を回し、1から40までの数字を1つずつ取り出し、変数iに格納していく
#   ※この先、チャッピーにヒントもらってから書いた
# iを文字列にキャストしたものを、変数i_strに格納
# iを3で割ったときの余りが0になる、かつ、iの先頭の数字が3である（i_strに文字列”3”が含まれる）場合は、
# iをthreeの要素として追加
# for文の外で、printで「作成したリスト :three」を出力

three = []
for i in range(1, 41):
    i_str = str(i)
    if i % 3 == 0 and "3" in i_str:    
    # 「"3" in i_str」を「i_str in "3"」と書いて失敗
    # 「"3" in i_str」だけでいいのに「 "3" in i_str == True」と書いて失敗　inはそれだけで完成品の条件式なので== Trueは不要！！
        three.append(i)
print(f'作成したリスト：{three}')

# 変数i_strを省くともっと簡素
three = []
for i in range(1, 41):
    if i % 3 == 0 and "3" in str(i):
                          #  str(i)これ、いったん他の変数に入れないとiの型が変わっちゃう…と心配していたのだが、i = str(i)にしてないから平気
        three.append(i)
print(f'作成したリスト：{three}')

print("-" * 20)# ----------
# 第1章の復習　※問題文は省略！

# ◎問題1
a = 7
b = 3
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} × {b} = {a*b}')
print(f'{a} ÷ {b} = {a//b} 余り {a%b}')
print(f'{a} ÷ {b} = {a/b}')

print("-" * 20)# ----------
# ×問題2・×問題3　➡　Googlecolabで実演

# ◎問題4
for i in range(1, 31):
    print(i) 

# 問題5  while文省略

print("-" * 20)# ----------
# ◎問題6
for t in range(1, 31):
    if t % 3 == 0:
        print(t)

print("-" * 20)# ----------
# ◎問題7
for n in range(1, 31):
    if n % 15 == 0:
        print("fizzbuzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print(n)

print("-" * 20)# ----------
# 問題8・9・10は次回復習






