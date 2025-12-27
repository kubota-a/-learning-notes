

# もっとスマートなコード　get関数を使うと、条件分岐を書く必要がなくなって4行が1行にできる！
w = input("文字を入力してください > ")
w_dict = {}
for i in w:
    w_dict[i] = w_dict.get(i, 0) + 1
print(w_dict)




