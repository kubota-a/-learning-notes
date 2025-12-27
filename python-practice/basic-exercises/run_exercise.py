# 別解　新たな文字列を作らずに、もとの文字列からダイレクトに母音を削除する方法
word = input("文字列を入力してください > ")
vowel_list = ["a", "i", "u", "e", "o"]
for w in vowel_list:    # 母音の入ったリストvowel_listをループの対象とする
    word = word.replace(w, "")
    print(word)
print(f'作成した文字列 : {word}')