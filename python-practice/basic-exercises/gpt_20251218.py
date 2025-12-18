# 問題1
scores = {
    "Alice": 82,
    "Bob": 58,
    "Charlie": 90,
    "Diana": 70,
    "Eve": 65
}
# 70点以上の人だけを 合格者リスト として作成せよ
# 合格者リストには 名前（文字列）だけ を入れること
# 最後にそのリストを出力せよ
passed_names = []    # 空のリストpassed_namesを定義　●[]を()と書いてエラーが出た
for name in scores.keys():    # scoresのすべてのキーを1つずつ取り出して変数nameに格納　●.keysの後ろに()を付け忘れてエラーが出た
    if scores[name] >= 70:    # scoresの該当Valueを取得し、70以上かどうかを判定。70以上なら、
        passed_names.append(name)    # リストpassed_namesにnameを追加する
print(passed_names)

print("-" * 20)# ----------
# 問題2
ages = [12, 18, 25, 9, 30, 15]
# 要求
# 「18歳以上の人数」を数えて出力せよ
# ただし 処理は関数として定義すること
# 条件
# 関数名は count_adults
# 引数としてリストを受け取る
# return で人数を返す

# 解答A　カウンタ変数を使う ▶　人数だけ欲しいとき
def count_adults(ages_list):    # リストages_listを受け取る関数count_adultsを定義
    adults = 0    # カウンタ変数adultsを0で初期化して宣言　●ここで変数adultsに初期値を入れていなかったせいで32行目「adults += 1」でエラーが出た
    for age in ages_list:    # ages_listの要素を1つずつ取り出して変数ageに格納
        if age >= 18:    # ageが18以上なら
            adults += 1    # 変数adultsに1を加算する
    return adults    # 変数adultsを戻り値として返す

ages = [12, 18, 25, 9, 30, 15]
adult_count = count_adults(ages)    # 変数adult_countに、引数agesを渡した関数count_adultsの戻り値を格納
print(adult_count)    # 変数adult_countの値を出力

del adult_count

# 解答B　18歳以上の要素を集めてからその長さを返す　▶　人数も欲しいし、人数の内訳も欲しい
def count_adults(ages_list):    # リストages_listを受け取る関数count_adultsを定義
    adult_list = []    # 空のリストadult_listを用意
    for age in ages_list:
        if age >= 18:
            adult_list.append(age)
    adults = len(adult_list)
    return adults

ages = [12, 18, 25, 9, 30, 15]
adult_count = count_adults(ages)
print(adult_count)

del adult_count

# 解答D　rangeを使う　※実務ではあまり使わないけど、学習用として一応書く！
def count_adults(ages_list):    # リストages_listを受け取る関数count_adultsを定義
    adult_list = []    # 空のリストadult_listを用意
    for i in range(len(ages_list)):    # リストages_listの要素数分の数字が入った袋をrange()で作成
        if ages_list[i] >= 18:    # もしages_lisの要素iが18以上なら
            adult_list.append(ages_list[i])    # adult_listにages_lisの要素iを追加する
    return len(adult_list)    # 戻り値としてadult_listの要素の数を返す

ages = [12, 18, 25, 9, 30, 15]
adult_count = count_adults(ages)
print(adult_count)







    
