# 解答2：重複する文字を各1つだけ拾うバージョン　→　str_1 = "banana"・str_2 = "an"なら出力が「an」になる
common_chars = ""
str_1 = input("1つ目の文字列を入力してください > ")
str_2 = input("2つ目の文字列を入力してください > ")
for i in str_1:
    if i in str_2 and i not in common_chars:    # iがstr_2に含まれる、かつ、common_charsには含まれない場合、
        common_chars += i
    elif i in str_2 and i in common_chars:    # iがstr_2に含まれる、かつ、common_charsにも含まれる場合、
        continue
print(f'重複する文字列 : {common_chars}')